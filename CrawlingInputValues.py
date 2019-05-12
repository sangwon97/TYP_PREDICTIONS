# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from selenium import webdriver
from TyphoonList import *
from TyphoonListfunc import *
import time
import pymysql

# db_connect information
_host = '168.131.39.95'
_port = 3306
_user = 'root'
_passwd = 'jslab0963'
_db = 'TYP'

# access
db = pymysql.connect(host=_host, port=_port, user=_user, passwd=_passwd, db=_db, charset='utf8')
cursor = db.cursor()

for ni in name_index:

    sql = "SELECT * FROM " + ni
    cursor.execute(sql)
    result = cursor.fetchall()
    
    for row_data in result:
        _date = str(row_data[0])[0:10].replace("-","/")
        _time = str(row_data[0])[11:16].replace(":","")
        latitude = str(row_data[1])
        longitude = str(row_data[2])
        
        driver = webdriver.Chrome('/Users/sangwon/Documents/chromedriver')
        driver.get('https://earth.nullschool.net'\
                   '/#' + _date + '/' + _time + 'Z'\
                   '/wind/surface/level/overlay=temp/orthographic'\
                   '/loc=' + longitude + ',' + latitude)
        time.sleep(5)        
        html = driver.page_source
                 
        soup = BeautifulSoup(html, 'html.parser')
        WD = (soup.select('#location-wind')[0].text).split(' @ ')[0].replace("°","")
        WV = (soup.select('#location-wind')[0].text).split(' @ ')[1]
        WT = soup.select('#location-value')[0].text
        
        
        sql2 = "UPDATE " + ni + " SET WD = '" + WD + "', WV = '" + WV + "', WT = '" + WT + "' WHERE Date = '" + str(row_data[0]) + "';"
              
        # 실행하기
        cursor.execute(sql2)
        
        # DB에 Complete 하기
        db.commit()
        
        driver.quit()


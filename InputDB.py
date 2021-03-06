# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 19:56:07 2019

@author: sangwon
"""

import pymysql
from TyphoonList import *
from TyphoonListfunc import *

# db_connect information
_host = '168.131.39.95'
_port = 3306
_user = 'root'
_passwd = 'jslab0963'
_db = 'TYP'

# access
db = pymysql.connect(host=_host, port=_port, user=_user, passwd=_passwd, db=_db, charset='utf8')

# 커서 가져오기
cursor = db.cursor()

result = callTyphoonInformation(index)
count = 0

for rst in result:
    
    result2 = rst['information']

    for idx in result2:
        
        sql = "INSERT INTO " + name_index[count] + " (Date, Latitude, Longitude) VALUES (%s, %s, %s);"  
          
        # 실행하기
        cursor.execute(sql, (idx['Date'], idx['latitude'], idx['longitude']))
        
        # DB에 Complete 하기
        db.commit()

    count += 1

# DB 연결 닫기
db.close()
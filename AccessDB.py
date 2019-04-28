# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 16:50:12 2019

@author: sangwon
"""

import pymysql
from TyphoonList import *

# db_connect information
host = '168.131.39.95'
port = 3306
user = 'root'
passwd = 'jslab0963'
db = 'Typhoons'

# access
db = pymysql.connect(host, port, user, passwd, db, charset='utf8')

# 커서 가져오기
cursor = db.cursor()

for idx in name_index:
    typhoonname = str(idx);
    sql = " CREATE TABLE " + typhoonname + " (\
            Date DATETIME NOT NULL,\
            Latitude DECIMAL(4, 1) NOT NULL,\
            Longitude DECIMAL(4, 1) NOT NULL,\
            WD INT UNSIGNED,\
            WT INT,\
            PRIMARY KEY(Date)); "
        
    # 실행하기
    cursor.execute(sql)
    
    # DB에 Complete 하기
    db.commit()


# DB 연결 닫기
db.close()





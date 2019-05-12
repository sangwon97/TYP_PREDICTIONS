# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 16:50:12 2019

@author: sangwon
"""

import pymysql
from TyphoonList import *

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

for idx in name_index:
    typhoonname = str(idx);
    sql = " CREATE TABLE " + typhoonname + " (\
            Date DATETIME NOT NULL,\
            Latitude DECIMAL(4, 1) NOT NULL,\
            Longitude DECIMAL(4, 1) NOT NULL,\
            WD INT UNSIGNED,\
            WV DECIMAL(6,3),\
            WT DECIMAL(6,3),\
            PRIMARY KEY(Date)); "
        
    # 실행하기
    cursor.execute(sql)
    
    # DB에 Complete 하기
    db.commit()


# DB 연결 닫기
db.close()





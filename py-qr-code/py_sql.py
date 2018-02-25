#! /usr/bin/env python
#-*- coding: UTF-8 -*-
import MySQLdb
def connection():
    coon=MySQLdb.connect(host='150.95.216.176',port=3306,user='root',passwd='baobei1181213',db='test',charset='utf8')
    cur=coon.cursor()
    return cur

def getkey(cur):
    sql="select * from key_value"
    cur.execute(sql)
    result=cur.fetchall()
    return result

    

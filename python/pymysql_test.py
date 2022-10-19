'''
작성일 : 2020. 12. 28.
작성자 : 정성모
코드개요 : pymysql connect test
'''
import pymysql

speed_db = pymysql.connect(
            user='root', 
            passwd='1', 
            host='192.168.1.16', 
            db='updatedb', 
            port=3306,
            charset='utf8')
cursor = speed_db.cursor()
print(cursor)
print(type(cursor))

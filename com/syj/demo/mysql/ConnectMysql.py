# coding=utf-8

import MySQLdb

con = MySQLdb.connect(host='localhost', user='root', passwd='syjmysql2015', db='spider_db', port=3306,
                      charset='utf-8')
cur = con.cursor()
cur.execute('create table person(id int not null)')
print 'ok'
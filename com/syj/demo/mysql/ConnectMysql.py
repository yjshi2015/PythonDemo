# coding=utf-8

import MySQLdb

con = MySQLdb.connect(host='localhost', user='root', passwd='syjmysql2015', db='spider_db',
                      port=3306, charset='utf8')
cur = con.cursor()
'''
cur.execute('create table person_info(id int not null auto_increment primary key, '
            'name varchar(60),'
            'age int)')
'''
cur.executemany('insert into person_info(name,age) values(%s, %s)', [('syj', 18), ('jack', 20)])
con.commit()
print '--------->数据写入成功ok'

cur.execute('select * from person_info')
res = cur.fetchall()
for line in res:
    print line
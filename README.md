# PythonDemo
python学习备忘

# mysql安装步骤
 -1 sudo apt-get install mysql-server
 (过程中需要设置root用户的密码syjmysql2015)
 -2 sudo apt-get install mysql-client
 -3 sudo apt-get install libmysqlclient-dev
 -4 sudo netstat -tap | grep mysql
 (查看是否安装成功)
 -5 mysql -u root -p
 登录
 -6 create database spider_db character set gbk;
 创建数据库
 -7 use spider_db
 切换到对应的数据库上
 -8 sudo pip install MySQL-python
 python中使用MySQL

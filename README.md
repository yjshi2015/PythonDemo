# PythonDemo
python学习备忘

# mysql安装步骤
 - 1 sudo apt-get install mysql-server
 (过程中需要设置root用户的密码 \*\*\*mysql\*\*\*\*)
 - 2 sudo apt-get install mysql-client
 - 3 sudo apt-get install libmysqlclient-dev
 - 4 sudo netstat -tap | grep mysql
 (查看是否安装成功)
 - 5 mysql -u root -p
 登录
 - 6 create database spider_db character set gbk;
 创建数据库
 - 7 use spider_db
 切换到对应的数据库上
 - 8 sudo pip install mysql-python
 python中使用MySQL
 - 8.1 sudo apt-get install python-mysqldb
      pip install mysql-python
 上述第8步失败,故使用8.1方案,同样不行

# 配置MySQL
 - 1. 允许远程访问mysql，编辑文件/etc/mysql/mysql.conf.d/mysqld.cnf,注释掉bind-address = 127.0.0.1：  
      `sudo vi /etc/mysql/mysql.conf.d/mysqld.cnf`
 - 2. 进入MySQL服务
      `mysql -uroot -p`
 - 3. 允许指定用户访问：
      `GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'syjmysql2015' WITH GRANT OPTION;`
      (IP这里，可以使用%来表示所有IP)
       `flush privileges;`
 - 4. 执行quit命令退出mysql服务，
      `exit`
 - 5. 执行如下命令重启mysql：
      `service mysql restart`

# 安装MySQL客户端
 - 1. 可参考文章
      https://cloud.tencent.com/developer/article/1343695
 - 2. 使用slqyog工具,访问官网,注册下载免费版
      https://www.webyog.com/
 - 3. 使用navicat,官网
      http://www.navicat.com
 - 4. 
      
                
# 终端连接数据库
 - 1. `mysql -uroot -p`,再输入密码即可
 - 2. 
# mongodb安装步骤
  - 1 在opt目录下创建mongodb目录
  `mkdir /opt/mongodb`
  - 2 下载对应版本的mongodb到第一步创建的路径中
  https://www.mongodb.com/download-center/community
  - 3 解压文件到`/usr/local/mongodb`目录下
  `tar -zxvf /opt/mongodb/mongodb-xxx.tar /usr/local/mongodb`
  - 4 在`/ect/profile`中配置环境变量
  `export PATH="NEW_PATH1:NEW_PATH2:$PATH"`
  - 5 在`/opt/mongodb`目录下创建数据库对应的目录
  `mkdir /opt/mongodb/data/db`
  - 6 启动mongodb,先切换到mongodb的bin目录下
  `sudo ./mongod --dbpath /opt/mongodb/data/db`
  - 7 mongo后台管理shell,先切换到mongo的bin目录,然后执行
  `./mongo`
  - 8 使用Python链接mongo,则需要先安装驱动,如果提示权限不够,增加--user参数
  `pip install --user pymongo`

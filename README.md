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

# Python编码问题
  https://www.cnblogs.com/gengyantao/p/7808687.html
  
# PhantomJS
  - 1. 简介
      如果一个页面Ajax请求很多,有时请求参数还进行了加密,我们手动分析每一个Ajax请求,
      将成为一项繁重的工作.通过PhantomJS,可直接从浏览器提取渲染好的HTML文档,不进行
      Ajax请求分析.
      PhantomJS可以看做是一个没有界面的浏览器,它既有Firefox浏览器/Google浏览器的功能,
      又因为没有界面而更加快捷,占用更小内存
      PhantomJS是一个基于WebKit的服务器端JavaScript API.它全面支持web而无需浏览器支
      持,不仅运行快,原生支持各种Web标准:DOM处理/CSS选择器/JSON/Canvas和SVG,可用于页面
      自动化/网络检测/网页截屏以及无页面测试等.
  - 2. 下载安装
      地址:https://phantomjs.org/download.html
  - 3. 解压
      tar -xjvf /tmp/mozilla_syj0/phantomjs-2.1.1-linux-x86_64.tar.bz2 -C /usr/local/phantomJS/
  - 4. 配置环境变量
      `vim /etc/profile` 要重启后才生效

# Selenium
  - 1. Selenium是一个自动化测试工具,支持浏览器驱动,可以对浏览器进行控制.而且Selenium
  支持多种语言开发,比如Java/C/Ruby/Python,因此Python+Selenium+PhantomJS的组合就产
  生了.PhantomJS负责渲染解析JavaScript,Selenium负责驱动浏览器和Python对接,Python
  负责后期处理
  - 2.通过idea的project structure-\>sdk-\>package安装
  - 3.在Selenium官网下载Firefox浏览器驱动,比较难找:https://www.seleniumhq.org/download/
  - 4.解压到`/usr/local/firefoxDriver/`路径下
  - 5.配置环境变量 `sudo vim /etc/profile`,`source /etc/profile`使其立即生效
  
# JavaScript短路原理
  - 1. 针对&&
   + 只要“&&”前面是false，无论“&&”后面是true还是false，结果都将返“&&”前面的值;
   + 只要“&&”前面是true，无论“&&”后面是true还是false，结果都将返“&&”后面的值;
  - 2. 针对||
   + 只要“||”前面为false,不管“||”后面是true还是false，都返回“||”后面的值。
   + 只要“||”前面为true,不管“||”后面是true还是false，都返回“||”前面的值。
  - 3. 真假判断逻辑
   在js逻辑运算中，0、”“、null、false、undefined、NaN都会判为false，其他都为true
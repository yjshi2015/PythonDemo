# PythonDemo
python学习备忘

# 使用IDEA搭建Python开发环境
- 1. 在为每个项目设置Project Structures时,常常会遇到问题,即项目B在安装依赖包时,包的目录为项目A指定的SDK目录,
  导致项目B在运行时提示`no module named XXX`,所以需要设置全局的SDK,即指定Python解释器的路径为全局路径,而非
  在各子项目中设置Pyhton解释器

# 编码问题
  -1. 英语采用ASSIC码  后来有了中文,扩充后成了GBK编码,后来各个国家加入,于是ISO组织成立了Unicode编码(包含utf-8和utf-16)
  https://www.jianshu.com/p/67cdb878efcb
  https://www.cnblogs.com/lowmanisbusy/p/9135917.html

# 定时任务crontab
  -1. 通过`crontab -e`建立定时任务
      'Ctrl + O' 写入, 'Enter' 保存文件名, 'Ctrl + X' 退出
  -2. 可采用如下命令查看定时任务的执行log,`tail -f /var/log/cron.log`
  -3. 如果日志提示`mailed 80 bytes of output but got status 0X400b from MTA#02`,则通过如下设置,关闭发送邮件功能
      `command >/dev/null 2>&1`
  
  如果无cron.log文件,按如下操作开启定时任务服务
  +1.修改rsyslog文件：
    `sudo vim /etc/rsyslog.d/50-default.conf` 
　 　将  rsyslog  文件中的  #cron.*  前的  #  删掉；  
  +2.重启rsyslog服务：
  `service rsyslog restart` 
  +3.重启cron服务：　　
  `service cron restart`
  
  **注意事项:**
  1.首先一定要确认crontab表达式是否正确,否则你的任务执行周期并不是你以为的那样
    `1 * * * * command`是每小时的第1分钟执行,而不是每分钟执行!!!
  2.加**print日志**会引入新的问题,但往往很容易忽略,因为并没有该之前的逻辑所以这类问题就很难发现.
    可在终端单独执行`command`来确认是否有问题  
  
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

# Scrapy框架搭建
  -1 在Ubuntu中已经预装了lxml和OpenSSL,所以直接安装Scrapy即可
     `sudo pin install Scrapy`,在Shell中通过`scrapy`命令来验证是否安装成功
  -2 切换到相应的目录下,利用scrapy创建项目cnblogSpider
     `scrapy startproject cnblogSpider`
     
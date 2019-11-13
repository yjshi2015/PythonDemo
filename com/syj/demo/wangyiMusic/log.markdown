创建爬虫项目步骤

1. 进入要创建项目的包路径下,创建爬虫项目: `scrapy startproject wangyiMusic`
2. 进入爬虫项目包路径: `cd wangyiMusic`
3. 初始化爬虫脚本: `scrapy genspider -t crawl wangyiSpider 163.com`
4. 定义Item
5. 研究返回体:在命令框中`scrapy shell "https://music.163.com/discover"`查看页面请求情况
   然后将返回体保存到本地,并且用浏览器打开`view(response)`
   注意此种方式并不会触发对返回体中的异步请求,比如图片这些是无法加载出来的,导致通过浏览器看不到具体内容
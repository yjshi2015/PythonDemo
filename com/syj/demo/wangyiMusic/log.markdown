创建爬虫项目步骤

1. 进入要创建项目的包路径下,创建爬虫项目: `scrapy startproject wangyiMusic`
2. 进入爬虫项目包路径: `cd wangyiMusic`
3. 初始化爬虫脚本: `scrapy genspider -t crawl wangyiSpider 163.com`
4. 定义Item
5. 研究返回体:在命令框中`scrapy shell "https://music.163.com/discover"`查看页面请求情况
   然后将返回体保存到本地,并且用浏览器打开`view(response)`
   注意此种方式并不会触发对返回体中的异步请求,比如图片这些是无法加载出来的,导致通过浏览器看不到具体内容
6. 运行爬虫,验证返回体,在项目的根目录下:`scrapy crawl wangyiSpider`   


注意
1. 在写Xpath脚本时,在浏览器F12模式下看到的页面结构只能作为参考,并不代表真正URL(https://music.163.com/discover/toplist?id=2884035)
的返回内容,要看实际返回结果,应该在F12的"网络请求"中,找到该URL的返回结果进行分析,不要被其他相似的URL所迷惑

2. 爬虫对URL的返回结果是Unicode格式的,故在分析页面结构时,要先转成UTF8,否则会找不到你所期望的内容.

3. xpath对象进行extract后,就是普通的Python对象了,而非xpath对象.以下的逻辑中,要在for循环中再使用xpath的话,在response的xpath后,
就不能使用extract了
```
        songs = response.xpath("//*[@id='song-list-pre-cache']/ul/li")
        for song_item in songs:
            print song_item
            song_link = song_item.xpath(".//a/@href").extract()[0]
            song_name = song_item.xpath(".//a/text()").extract()[0]
            print song_link
            print song_name

```
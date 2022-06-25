# selenium
[官方文档](https://selenium-python.readthedocs.io/api.html#)
- 1.等待方式 
  - 隐式等待(不推荐) & 显示等待(推荐), **显示等待**：指定要查找的节点和最长等待时间。如果规定时间内加载出了要查找的节点，就返回这个节点；否则抛出超时异常
  - demo
  ```python
  from selenium.webdriver.support.ui import WebDriverWait
  from selenium.webdriver.support import expected_conditions as EC
  ……略……
  wait = WebDriverWait(browser, 10) #最长等待时间为10秒
  # 等待至id为xxx的节点出现
  input = wait.until(EC.presence_of_element_located((By.ID, '#xxx'))
  # 同上
  input = wait.until(EC.visibility_of_element_located((By.ID, '#xxx')))
  # 节点可点击
  button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
  ```
- 2.节点选择器
  - find_element:找到单个节点
  - find_elements：找到多个节点，返回值为list
  - demo
    - find_element\[s\](By.ID, '#xxx')
    - find_element\[s\](By.NAME, '#xxx')
    - find_element\[s\](By.TAG_NAME, '#xxx'),按照标签来查找
    - find_element\[s\](By.CLASS_NAME, '#xxx'),按照class name查找某个节点，采用全匹配的方式
    - find_element\[s\](By.CSS_SELECTOR, '#xxx'),按照css定位器查找某个节点，可横跨多个节点，最终定位到具体节点，最常用
    - find_element\[s\](By.XPATH, '#xxx')
- 3.获取节点信息
  - 前提是按照步骤2先获取某个节点
  - demo
    ```python
    # 获取图片的链接
    logo = browser.find_element(By.CLASS_NAME, 'logo-image')
    print(logo.get_attribute('src')) 
    
    # 获取文本值
    input = browser.find_element(By.CLASS_NAME, 'logo-title')
    print(input.text)
    
    # 获取ID/位置/标签名和大小
    print(input.id)
    print(input.location)
    print(input.tag_name)
    print(input.size)
    
    ```
- 4.切换iframe
  - @see com/syj/cuiqingcai/chapter7/selenium/SwitchFrame.py
- 5.cookie操作
  - @see com/syj/cuiqingcai/chapter7/selenium/HandleCookie.py
- 6.反屏蔽
  - 有些网站增加了对selenium的识别，防止一些爬虫的恶意爬取。检测的原理是检查当前浏览器窗口下的window.navigator对象中是否包含webdriver属性。因为在正常使用浏览器时，这个属性值undefined, 一旦使用了selenium/pypeetor/playwright等，就会给window.navigator对象设置webdriver属性。很多网站通过Javascript语句判断是否存在webdriver属性，如果有就屏蔽。
  - @see com/syj/cuiqingcai/chapter7/selenium/Selenium.py

# pyppeteer
[官方文档](https://pyppeteer.github.io/pyppeteer/reference.html)
- 1.等待方式，demo参见节点2
- 2.选择器，可以使用J方法（等价于querySelector）查询匹配到的第一个节点；或者JJ方法（等价于querySelectorAll），查询匹配到的所有节点
  - demo
  ```python
  import asyncio
  from pyppeteer import launch
  
  browser = await launch() 
  page = await browser.newPage() 
  
  await page.goto('xxxx')
  # 等待操作，让符合条件的节点加载出来再返回结果
  await page.waitForSelector('这里是CSS选择器语法')
  # 等待某个JavaScript方法执行完毕再返回
  await page.waitForFunction('xxx')
  # 等待某个特定的请求发出
  await page.waitForRequest('xxx')
  # 等待某个请求对应的结果
  await page.waitForResponse('xxx')
  
  # 选择节点
  result1 = await page.J('这里也是CSS选择器语法')
  result2 = await page.querySelector('这里也是CSS选择器语法')
  result3 = await page.JJ('这里也是CSS选择器语法')
  result4 = await page.querySelectorAll('这里也是CSS选择器语法')
  
  # 找出选择器匹配的节点，然后根据js定义的逻辑从这些节点中出去出对应的结果并返回
  result5 = await page.querySelectorAllEval('CSS选择器', 'JavaScrpt方法')
  ```
# Playwright是微软2020年开源的新一代自动化测试工具，具有众多优点：
[官网地址](https://playwright.dev/python/docs/api/class-selectors)
- 支持selenium的同步操作，也支持pyppeterr的异步操作
- 支持当前所有主流浏览器，chrome/Firefox/edge(基于chromium)/safari(基于webkit)
- 支持移动端页面测试
- 安装简单
- **代码自动生成**，牛逼到无以复加
- **最简洁的筛选器用法**
- demo
```python
  # 自动脚本命令 playwright codegen -o 脚本名 -b 浏览器类型
  playwright codegen -o auto_script.py -b chromium

  # 筛选器语法
  # css筛选器 + 文本值/节点关系
  page.click('筛选器', **kwargs) #点击操作,kwargs可设置点击次数/左右键等
  page.fill('筛选器', '输入的内容', **kwargs) # 输入
  element = page.query_selector('筛选器') #获取单个节点
  elements = page.query_selector_all('筛选器') #获取多个节点
  element.get_attribute('筛选器', '属性名称，比如href等') #获取属性
  ```
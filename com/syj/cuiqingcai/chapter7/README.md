# selenium
[官方文档](https://selenium-python.readthedocs.io/api.html#)
- 1.等待方式 
  - 隐式等待(不推荐) & 显示等待(推荐), **显示等待**：指定要查找的节点和最长等待时间。如果规定时间内加载出了要查找的节点，就返回这个节点；否则抛出超时异常
  - demo
  ```
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
    ```
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
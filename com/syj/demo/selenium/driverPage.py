# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 获取Firefox的浏览器驱动
driver = webdriver.Firefox()
# 调用get方法打开百度首页
driver.get('http://www.baidu.com')
assert u"百度" in driver.title
elem = driver.find_element_by_name("wd")
elem.clear()
elem.send_keys(u"银河补习班")
elem.send_keys(Keys.RETURN)
time.sleep(3)
assert u"邓超" in driver.page_source
driver.close()
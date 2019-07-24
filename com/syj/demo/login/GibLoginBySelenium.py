# coding=utf-8
import time
from selenium import webdriver

driver = webdriver.Firefox()
driver.set_page_load_timeout(5)
driver.get('https://github.com/login')

eleUserName = driver.find_element_by_id('login_field')
eleUserName.clear()
eleUserName.send_keys('495054021@qq.com')
eleUserName.click()

elePW = driver.find_element_by_id('password')
elePW.click()
elePW.send_keys('syjgit2015')
elePW.click()

eleSubmit = driver.find_element_by_name('commit')
eleSubmit.click()

# 等待所有的资源加载完毕
time.sleep(10)

html = driver.page_source

print html
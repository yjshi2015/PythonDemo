from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
print(browser.get_cookies())

browser.add_cookie({'name': 'syj', 'domain': '.zhihu.com', 'value': 'haha'})
print(browser.get_cookies())
browser.delete_all_cookies()
print(browser.get_cookies())
time.sleep(3)
browser.close()
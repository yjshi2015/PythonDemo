# coding=utf-8

import codecs
import datetime
from bs4 import BeautifulSoup

from selenium import webdriver
import selenium.webdriver.support.ui as ui
import selenium.webdriver.common.by as By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

class CtripSpider(object):

    def get_hotel(self, driver, to_city, fromdate, todate):

        ele_toCity = driver.find_element_by_id('txtCity')
        ele_fromDate = driver.find_element_by_id('txtCheckIn')
        ele_toDate = driver.find_element_by_id('txtCheckOut')
        ele_search = driver.find_element_by_id("btnSearch")
        ele_toCity.clear()
        ele_toCity.send_keys(to_city)
        ele_toCity.click()
        ele_fromDate.clear()
        ele_fromDate.send_keys(fromdate)
        ele_fromDate.click()
        ele_toDate.clear()
        ele_toDate.send_keys(todate)
        ele_toDate.click()
        ele_search.click()
        page_num = 0
        while True:
            try:
                WebDriverWait(driver, 10).until(
                    EC.title_contains(unicode(to_city))
                )
            except Exception, e:
                print ('----->等待10s失败', e)
                break
            time.sleep(5)

            # 分两次获取一页完整的数据,第二次让driver执行js脚本,把网页拉到底部
            js = "window.scrollTo(0, document.body.scrollHeight);"
            driver.execute_script(js)
            time.sleep(5)

            htm_const = driver.page_source
            soup = BeautifulSoup(htm_const, 'html.parser', from_encoding='utf-8')
            infos = soup.find_all(class_="hotel_new_list J_HotelListBaseCell")
            f = codecs.open(unicode(to_city)+unicode(fromdate)+u'.html', 'a', 'utf-8')
            for info in infos:
                f.write(str(page_num) + '--'*50)
                print ('info----------->', info)
                content = info.get_text().replace(" ", "").replace("\t", "").strip()
                for line in [ln for ln in content.splitlines() if ln.strip()]:
                    f.write(line)
                    f.write('\r\n')
            f.close()

            # 加载下一页
            try:
                next_page = WebDriverWait(driver, 20).until(
                    EC.visibillity_of(driver.find_element_by_id("downHerf"))
                )
                next_page.click()
                page_num += 1
                time.sleep(10)
            except Exception, e:
                print (u'------->加载'+str(page_num)+u'页数据失败', e)
                break

    def crawl(self, root_url, to_city):
        today = datetime.date.today().strftime('%Y-%m-%d')
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        tomorrow = tomorrow.strftime('%Y-%m-%d')
        driver = webdriver.Firefox()
        driver.set_page_load_timeout(50)
        driver.get(root_url)
        # 将浏览器最大化显示
        driver.maximize_window()
        # 控制间隔时间,等待浏览器反应
        driver.implicitly_wait(10)
        self.get_hotel(driver, to_city, today, tomorrow)


if __name__ == '__main__':
    spider = CtripSpider()
    # spider.crawl('http://hotel.qunar.com/', u"北京")
    spider.crawl('https://hotels.ctrip.com/hotel/beijing1#ctm_ref=ctr_hp_sb_lst', u"北京")
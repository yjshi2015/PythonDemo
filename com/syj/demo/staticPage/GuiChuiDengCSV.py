# coding=utf-8
import requests
from bs4 import BeautifulSoup
import re
import csv

try:
    user_aget='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0'
    headers={'User-Agent': user_aget}
    r = requests.get('http://seputu.com', headers=headers)
    # print r.text

    soup = BeautifulSoup(r.text, 'html.parser', from_encoding='utf-8')
    rows = []
    for mulu in soup.find_all(class_='mulu'):
        h2 = mulu.find('h2')
        if h2 != None:
            # 获取标题
            h2_title = h2.string.encode('utf-8')
            # [2012-5-19 3:3:52] 七星鲁王 第一章 血尸
            pattern = re.compile(r'\s*\[(.*)\]\s+(.*)')
            # 获取所有a标签中的URL和标题
            for a in mulu.find(class_='box').find_all('a'):
                href = a.get('href').encode('utf-8')
                box_title = a.get('title')
                match = pattern.search(box_title)
                if match != None:
                    date = match.group(1).encode('utf-8')
                    real_title = match.group(2).encode('utf-8')
                content = (h2_title, real_title, href, date)
                print content
                print h2_title, real_title, href, date
                rows.append(content)

    # 将结果转化为csv文件
    headers = ['title', 'chapter_title', 'href', 'date']
    with open('syj.csv', 'w') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rows)
except Exception as e:
    print e
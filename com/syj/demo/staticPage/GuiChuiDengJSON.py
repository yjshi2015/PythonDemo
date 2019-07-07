# coding=utf-8
import requests
from bs4 import BeautifulSoup
import json

try:
    user_aget='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0'
    headers={'User-Agent': user_aget}
    r = requests.get('http://seputu.com', headers=headers)
    # print r.text

    soup = BeautifulSoup(r.text, 'html.parser', from_encoding='utf-8')
    contents = []
    for mulu in soup.find_all(class_='mulu'):
        print '============mulu'
        h2 = mulu.find('h2')
        if h2 != None:
            # 获取标题
            h2_title = h2.string
            print h2_title
            list = []
            # 获取所有a标签中的URL和标题
            for a in mulu.find(class_='box').find_all('a'):
                href = a.get('href')
                box_title = a.get('title')
                print href, box_title
                list.append({'href': href, 'box_title': box_title})
            contents.append({'title': h2_title, 'content': list})

    # 将结果转化为json文件
    with open('syj.json', 'wb') as fp:
        json.dump(contents, fp=fp, indent=4)
except Exception as e:
    print e
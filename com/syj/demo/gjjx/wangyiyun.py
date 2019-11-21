# coding=utf-8

import requests
from urllib import urlencode
import json
from datetime import datetime

from email.header import Header
from email.mime.text import MIMEText
import smtplib
import sys

defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)


def _query_ks_info():
    try:

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
        response = requests.get('https://music.163.com/discover/toplist?id=2884035', headers=headers)
        result = response.text
        print result
        return result
    except Exception, e:
        print '获取课时列表信息失败'
        print e
        return None


if __name__ == '__main__':
    # 1.查询课时信息
    subscribeInfo = _query_ks_info()

    print 'end'

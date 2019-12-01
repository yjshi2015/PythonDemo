# coding=utf-8

import requests
from urllib import urlencode
import json
from datetime import datetime

from email.header import Header
from email.mime.text import MIMEText
import smtplib
import sys
import re

import com.syj.demo.wangyiMusic.wangyiMusic.spiders.encSecParams as enc

defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)


def _query_ks_info():
    try:
        url = 'https://music.163.com/weapi/v1/resource/comments/R_SO_4_1404884182?csrf_token=';
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
            'Referer': 'https://music.163.com/'}
        text = {"rid": "R_SO_4_1404884182", "offset": "0", "total": "true", "limit": "20", "csrf_token": ""}
        text = json.dumps(text)
        # 用于AES对称加密,作为首次加密的密钥
        nonce = '0CoJUm6Qyw8W8jud'
        # 用于RSA非对称加密的客户端公钥
        modulus = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
        pubKey = '010001'

        # 将js的加密逻辑通过Python来实现,步骤如下:
        # 1.随机生成AES加密的密钥secKey
        # 2.nonce也是AES加密的密钥,服务端和客户端同时持有,先用nonce将json形式的参数进行AES加密,加密后得到密文,
        # 再和随机生成的AES密钥secKey进行二次加密,此时的密文作为params参数
        # 3.用客户端持有的RSA的公钥pubKey,将随机生成的AES密钥secKey进行RSA非对称加密,得到encSecKey传到服务端
        secKey = enc.createSecretKey(16)
        encText = enc.aesEncrypt(enc.aesEncrypt(text, nonce), secKey)
        encSecKey = enc.rsaEncrypt(secKey, pubKey, modulus)
        data = {'params': encText, 'encSecKey': encSecKey}
        response = requests.post(url=url, headers=headers, data=data)
        result = response.text
        print result
        return result
    except Exception, e:
        print '获取课时列表信息失败'
        print e
        return None


if __name__ == '__main__':
    # 1.查询课时信息
    # subscribeInfo = _query_ks_info()
    url = 'http://music.163.com/songId=123'
    pattern = re.compile(r'=\d+')
    result = re.search(pattern, url)
    if result:
        song_id = result.group()[1:]
        print song_id

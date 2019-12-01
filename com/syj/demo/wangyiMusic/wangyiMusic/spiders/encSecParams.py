# -*- coding: utf-8 -*-

from Crypto.Cipher import AES
import base64
import os
import json

# AES对称加密,即加密和解密的密钥是同一个,加密的过程会有位移/偏移这样的操作
# todo 优缺点
def aesEncrypt(text, secKey):
    pad = 16 - len(text)%16
    text = text + pad*chr(pad)
    encryptor = AES.new(secKey, 2, '0102030405060708')
    ciphertext = encryptor.encrypt(text)
    ciphertext = base64.b64encode(ciphertext)
    return ciphertext


# RSA非对称加密,即客户端拥有公钥pubkey,通过公钥对明文加密,服务端通过私钥解密
# todo 优缺点
def rsaEncrypt(text, pubKey, modulus):
    text = text[::-1]
    # print text
    # print int(text.encode('hex'), 16)
    # print int(pubKey, 16)
    # print int(modulus, 16)
    rs = int(text.encode('hex'), 16)**int(pubKey, 16)% int(modulus, 16)
    # print format(rs)
    # print format(rs, 'x')
    return format(rs, 'x').zfill(256)


def createSecretKey(size):
    return 'ffffffffffffffff'
    # return (''.join(map(lambda xx:(hex(ord(xx))[2:]), os.urandom(size))))[0:16]


# text = {"rid": "R_SO_4_1404884182", "offset": "0", "total": "true", "limit": "20", "csrf_token": ""}
def encRequest(text):
    try:
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
        secKey = createSecretKey(16)
        encText = aesEncrypt(aesEncrypt(text, nonce), secKey)
        encSecKey = rsaEncrypt(secKey, pubKey, modulus)
        data = {'params': encText, 'encSecKey': encSecKey}
        return data
    except Exception, e:
        print '参数加密失败, text: ' + text + ', 失败原因: ' + e.message
        return None
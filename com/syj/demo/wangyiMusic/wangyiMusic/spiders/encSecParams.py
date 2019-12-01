# -*- coding: utf-8 -*-

from Crypto.Cipher import AES
import base64
import os

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
    print text
    print int(text.encode('hex'), 16)
    print int(pubKey, 16)
    print int(modulus, 16)
    rs = int(text.encode('hex'), 16)**int(pubKey, 16)%int(modulus, 16)
    print format(rs)
    print format(rs, 'x')
    return format(rs, 'x').zfill(256)


def createSecretKey(size):
    return 'ffffffffffffffff'
    # return (''.join(map(lambda xx:(hex(ord(xx))[2:]), os.urandom(size))))[0:16]
# coding=utf-8

import json

ip_word_set = {}
ip_word_set['王俊凯'] = '王俊凯'
ip_word_set['俊凯'] = '王俊凯'
ip_word_set['凯凯'] = '王俊凯'
ip_word_set['小凯'] = '王俊凯'

print ip_word_set
print json.dumps(ip_word_set, encoding='utf-8', ensure_ascii=False)
for item in ip_word_set.values():
    print item

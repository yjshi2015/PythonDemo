# coding=utf-8

import re
import requests


def get_token(session):
    index_url = 'https://github.com/login'
    index_page = session.get(index_url, headers=headers)
    html = index_page.text
    pattern = r'name="authenticity_token" value="(.*?)"'
    token = re.findall(pattern, html)
    return token[0]


user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0'
headers = {'User-Agent': user_agent}
session = requests.session()
token = get_token(session)

post_url = 'https://github.com/session'
post_data = {
    'commit': 'Sign+in',
    'utf8':	'✓',
    'authenticity_token': token,
    'login': '495054021@qq.com',
    'password':	'syjgit2015',
    'webauthn-support':	'supported'
}
login_page = session.post(post_url, data=post_data, headers=headers)
login_code = login_page.text
print login_page.status_code
print login_code
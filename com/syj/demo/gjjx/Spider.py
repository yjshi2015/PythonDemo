# coding=utf-8

import urllib2
import json
from datetime import datetime

from email.header import Header
from email.mime.text import MIMEText
import smtplib


def _query_ks_info():
    try:
        opener = urllib2.build_opener()
        # cookie信息应该为APP端写死的,即使退出重新登录,也没有变化
        opener.addheaders.append(('Cookie', 'JX_LoginOn=tHuIebKocq7tY383VvWrWHJFWnlpWJoeMboCCJ16XDb4PzhD7s8E9UFRmhLSFkVsqJ1DaxQtJ//RNxi4q1B4SHzx2aULiPmHh9WgSbVDpz0h4Nx777AE6V0wF/cWpyJWs6DJvP8+NipLkjBixQbLq36OOTqHe8pWqmkYyfxbobpDA4mPPVYXOHWlYw3WRHzfjwgPBMhCbWMbhGqdj3+Rn13kA4Tm6lrOHl9F3gAn//McKEvAcz3SxG80wx2nIQQUdATT55kCfy2YJLreNj3QumQpzFX0a4zDDhy9+sBuG7MkTTbunmGvpqW5Jc7A5c+I8wakpcdiN8AhWKDiKg0QKeF/MP/UDZm+kII7W0+IbdCABe2kay0RHtqBMAp0YVBH4J2qT12qhYv+47MgwedQy165hgtleEL4CbiIzNBQOPbQe+vybSjgese5yJEPu1ED5iFmdnvycyOvVokxN7xReRDujOaRC7Q9AKff1ZwlWlB4f5wNR5culFA7uiryvlpqxE0HxRfQT+Y=; '
                                            'yunsuo_session_verify=638febcbca91dd4671b5fed013b04551; '
                                            'Webapi_LoginOn_client=%7b%0d%0a%20%20%22userName%22%3a%20%2217710142680%22%2c%0d%0a%20%20%22phoneNum%22%3a%20%2217710142680%22%2c%0d%0a%20%20%22nickName%22%3a%20%22%e7%94%a8%e6%88%b7_5820%22%2c%0d%0a%20%20%22Id%22%3a%20%221228356%22%2c%0d%0a%20%20%22os%22%3a%20null%2c%0d%0a%20%20%22password%22%3a%20null%2c%0d%0a%20%20%22passwordmd5%22%3a%20%2283659067361aee75ff32805f05f82b01%22%2c%0d%0a%20%20%22xxzh%22%3a%20%2263335047%22%2c%0d%0a%20%20%22jgid%22%3a%20%22124001%22%2c%0d%0a%20%20%22webapiurl%22%3a%20null%2c%0d%0a%20%20%22xybh%22%3a%20%225101202569%22%2c%0d%0a%20%20%22sfzh%22%3a%20%22140225198410070024%22%2c%0d%0a%20%20%22jxcode%22%3a%20%22340800035%22%2c%0d%0a%20%20%22schoolpwd%22%3a%20%22rmzhao520%22%2c%0d%0a%20%20%22iconpath%22%3a%20null%2c%0d%0a%20%20%22username%22%3a%20%2217710142680%22%2c%0d%0a%20%20%22phonenum%22%3a%20%2217710142680%22%2c%0d%0a%20%20%22nickname%22%3a%20%22%e7%94%a8%e6%88%b7_5820%22%2c%0d%0a%20%20%22sinauid%22%3a%20null%2c%0d%0a%20%20%22apiurl%22%3a%20%22bookingcarapi%3a%3ahttp%3a%2f%2fgongjiaoapi.xuechebu.com%22%2c%0d%0a%20%20%22apiurlios%22%3a%20%22https%3a%2f%2fgongjiaoapi.xuechebu.com%22%2c%0d%0a%20%20%22jxmc%22%3a%20%22%e5%85%ac%e4%ba%a4%e9%a9%be%e6%a0%a1%22%2c%0d%0a%20%20%22xm%22%3a%20%22%e8%b5%b5%e7%9d%bf%e6%95%8f%22%2c%0d%0a%20%20%22usertype%22%3a%20%221%22%2c%0d%0a%20%20%22clientCode%22%3a%20null%2c%0d%0a%20%20%22dz%22%3a%20null%2c%0d%0a%20%20%22SQCX%22%3a%20%22C2%22%2c%0d%0a%20%20%22SSBX%22%3a%20%22%e8%87%aa%e5%8a%a8%e6%8c%a1%e5%85%a8%e5%91%a8%e9%a2%84%e7%ba%a6%e7%8f%ad%22%2c%0d%0a%20%20%22SchoolMasterUrl%22%3a%20%22%22%2c%0d%0a%20%20%22wxbindtype%22%3a%20%220%22%2c%0d%0a%20%20%22stunum%22%3a%20%22%22%0d%0a%7d; '
                                            'Webapi_LoginOn=nA0X2LvcDSa8FUGatP/A3nVv95zlVSBfSfZINMZAEPwRNzXf8SecTPdrDIglYbJzScFA7ZybwDBaIXocINBkTLA+P4Cf46k2cr8axOS/IF/jdTUzdv+Iol4xjJJENpZZZvakit/sRB/Q9UrCqM+C3iwvUvX51nrep5lYHX3t559UpMQ28UkbMCFPnRTGowSI0JfMnf5UaqzbqsnYwTupoeLxi/4eth68yHE6JtvGNZdrJoNHN1USwH5+9T+0sydNhCKpLrmgaelO41q+nBCdmrVAR34pvWYTdTUNZnnZGRMKXEnmU8mOBofhLhwTIoTu/7CJiFBa7Z5J/eQsO/vSew5c6XU4SWAD2/OyGlZGcWpATJNXToibkn+d/hjG5517sXAtMIl1iiSBgfB9Zunrw88SdKd5Fj/bKvTvyWWW9mFpoot0bUsVaux6s2uuqq6zt/1PRBlvSPdVCBEYffr4GzUwGIcclQ6cXQniKQRCmnhjWEyXM4HIsHYlN4/UcWrChCje7uWLlPemOSp06chuZcBVinXP6mY8+njd5csmHN1JwUDtnJvAMFohehwg0GRMdyL9bNntqJHTXdRw2tXs5PAGpSnlI3I1ae7+vmkJZUu6alHUKdPPaiQC3OWRwYWol70RcK4MALeit1QHan1tzaXcjUG0aDXtpk+M1hfqIFO7V/FESE/BW6EEs7yg9uaYNp6ZcSYr9CqP+RvsPlxJL2Gq037RvJ6zWhzbZe8U/mKlXm0wT1DO4dL+V0rmARBeiWbjl1sY3rpQSCtI8hw73YlIiCcXlCUXTQyRrWtOVZXXMF0ZbQQAJOUjj86Y0C5SW4Ll3MC37vptch9DkGwybGbtjTDUKSnCLLg12DgYevSbGJy9W4gCv2ngoZwA3XkI5S8r8czX7YpvMpPXEKWADN/UuMYg/EaJDZQsl6KVURqmT4zWF+ogU3refYS2tq89xie+G8y76b7rRwOcwWVO9Gzhqk48VooftCTz9kqoy2GEy5F2nGL9/asvfbC2wuONdzLnLaQGwt6Tm32ZeLiCLdk8XRqYGrBYMyLklKoLOWGpdI9N3D1dw7dFyl9zjd6tsXAtMIl1iiS8SkvyV8n6bevfzoG0/0Nx'))
        opener.addheaders.append(('User-Agent', 'android_gongjiao;v4.1.0;'))
        opener.addheaders.append(('Host', 'gongjiaoapi.xuechebu.com'))
        opener.addheaders.append(('Connection', 'Keep-Alive'))
        req = urllib2.Request('http://gongjiaoapi.xuechebu.com/KM2/ClYyTimeSectionUIQuery2?'
                              'trainType=3&osversion=6.0&ossdk=23'
                              '&imei=ABCD6AF787AD26ASDFGADB8F6143B8880'
                              '&xxzh=63335047'
                              '&appversion=4.1.0&version=4.1.0'
                              '&ipaddress=192.168.66.2&tcqy=null&os=an')
        response = opener.open(req)
        return response.read()
    except Exception, e:
        print '获取课时列表信息失败' + e
        return None


def _parse_ks_info(subscribeInfo):
    jsonObj = json.loads(subscribeInfo)
    detail = jsonObj.get('data').get('UIDatas')
    leftKSList = []
    for item in detail:
        yyrq = item.get('Yyrq')  # 预约日期
        xnsd = item.get('Xnsd')  # 校内时段, 812: "07:00--11:30", 15: "12:30--17:00", 58": "17:45--20:45"

        sl = item.get('SL')
        # 排除 晚上的时段,或者剩余课时为0的
        if int(xnsd) == 58 or int(sl) == 0:
            continue
        week = datetime.strptime(yyrq.encode('utf-8'), "%Y/%m/%d %H:%M:%S").weekday()
        if week == 5 or week == 6:
            leftKSInfo = {'date': yyrq.encode('utf-8') + " 是周 " + (week + 1), 'message': "赶紧动手预约吧"}
            leftKSList.append(leftKSInfo)
            print yyrq.encode('utf-8') + "---" + str(week)
    return leftKSList


def _send_mail(body):
    # 发件人地址
    from_addr = '495054021@qq.com'
    # 邮箱密码
    password = 'syjqq2015'
    # 收件人地址
    to_addr = '495054021@qq.com'
    # qq邮箱服务器地址
    smtp_server = 'smtp.qq.com'
    # 设置邮箱信息
    msg = MIMEText(','.join(body), 'plain', 'utf-8')
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = Header('周末白天有课时啦', 'utf-8').encode()

    # 发送邮件
    server = smtplib.SMTP(smtp_server, 25)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()


if __name__ == '__main__':
    # 1.查询课时信息
    subscribeInfo = _query_ks_info()
    if subscribeInfo is not None:
        # 2.解析课时信息
        leftKSList = _parse_ks_info(subscribeInfo)
        # 3.发送邮件通知
        if len(leftKSList) > 0:
            print '有课时' + leftKSList
            _send_mail(leftKSList)
        else:
            print '没有课时啦'

    print 'end'

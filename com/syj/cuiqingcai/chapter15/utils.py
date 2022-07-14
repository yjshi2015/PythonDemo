import base64

tmp = base64.b64decode('SmQ0RcLLLxron3RTk19DhQ=='.encode('utf-8'))
print(tmp)

'''
RSA私钥：动态获取
MIICdgIBADANBgkqhkiG9w0BAQEFAASCAmAwggJcAgEAAoGBANjLpuUMXeXll0L2\nqd/GaQWlpk3YtgmNGdZZzlgPREMLXoem9QJXH4F3RW8tD7hrurZZxCGmvaK+XNKd\n6TZlUZV0SG8VNDzoZGm2LOFI8M+DcHKjVXItUZWGPQeK/9mwZ6XVbMXG5wcpAtvf\nHc8gx8D0FsLA+gIP5tkLvGW4UpTnAgMBAAECgYAs+NoPK6iS1zSwnHCSzhrdJAbC\noVDp3E5ey9RlKg2UBti+NSEgMiiD99T8ghF/xUE/MJHiFS/Dgc/JlR5avVvVzkDK\n0bqY08iCdBHzw9l7ftzcgAg3Pq/kYg1bSecwX/+eSkSy9CKFlMa5K1ElbkfWIIT8\nr79hrYSTj92IKC4BEQJBAO6oakxkEBY5kmQXXmZaJd/+lxlFzf0rBENK07765Tu1\npex2iGPkJbcAx9z4p1q2SUYIt1B3xnVxqdmDIUcdvSkCQQDojIvwiaAwH/2ER0Ox\nn+u1QGu54IDm0oHIr1Q31WJKU7D5kg6/MjnKzopM7wqY6GP+0Qe3T1hNh9Mze8t/\n6POPAkAwjKozKBftrYCORAK8J5KU4qGyTnT9D4cqeUpiC4AeiXFbjTFpwLu7YrlF\nxn+lAHgfex5vjC4fLiQzT22xnechAkEAyXrD3/KNjESbNJk96E5jPNWEwDXn2JS4\nB3UIpZtGHpmmMoS+LB9K/RC3uHI/Hz3xLRxT8BlZq0qrzOZL6RWetwJALTr7sZvI\nmpZRPC+VADx4wn8E2t02459wr6zFyqF0WRnel3OF5bAIpDZNoDoA7gCCwmtU293l\npc6uixENXcmW5g==


0、URL
https://web-001.cloud.servicewechat.com/wxa-qbase/container_service?token=58_kqGZl5Ws6O5tdDGBOv7u926A61ey0Bs7BV_hBa4ZEFsReFteK_52f9itR3Yi6j8bG2EhZtAXaeMG4rwb

1、header
Content-Type: "application/octet-stream"
X-WX-COMPRESSION: "snappy"
X-WX-ENCRYPTION-TIMESTAMP: "1657330658093" # 时间戳
X-WX-ENCRYPTION-VERSION: 2
X-WX-LIB-BUILD-TS: 1655460325335
X-WX-REQUEST-CONTENT-ENCODING: "JSON"
X-WX-RESPONSE-CONTENT-ACCEPT-ENCODING: "PB, JSON"
X-WX-USER-TIMEOUT: 30000

2、data
L.buffer
L = D.AES_CBC.encrypt(N, x, void 0, x)
                                  
# x的来源，依赖i
var x = new Uint8Array(s.base64ToArrayBuffer(i.key))

# i的demo1
{
cloudServiceUrl: undefined
domain: "web-001.cloud.servicewechat.com"
expiresTs: 1657332458732
http: true
ip: undefined
key: "fTzwkb5Kig+s8E42Zk4sIQ=="
timestamp: 1657330658093
token: "58_kqGZl5Ws6O5tdDGBOv7u926A61ey0Bs7BV_hBa4ZEFsReFteK_52f9itR3Yi6j8bG2EhZtAXaeMG4rwb"
url: "https://web-001.cloud.servicewechat.com/wxa-qbase/container_service?token=58_kqGZl5Ws6O5tdDGBOv7u926A61ey0Bs7BV_hBa4ZEFsReFteK_52f9itR3Yi6j8bG2EhZtAXaeMG4rwb"
vip: "109.244.145.199"
}

# i的demo2
cloudServiceUrl: undefined
domain: "web-001.cloud.servicewechat.com"
expiresTs: 1657334098078
http: true
ip: undefined
key: "l8Mj6oJ4WgiJnTJmG4lIbw=="
timestamp: 1657332297419
token: "58_e-KmY-dguy9AI7AJPjJ3FK1DDCHUnpp31WqzqU3wRLye1M0kErRAa99oBGOAeiJnx9s6E4h1REg9NIlZ"
url: "https://web-001.cloud.servicewechat.com/wxa-qbase/container_service?token=58_e-KmY-dguy9AI7AJPjJ3FK1DDCHUnpp31WqzqU3wRLye1M0kErRAa99oBGOAeiJnx9s6E4h1REg9NIlZ"
vip: "109.244.145.199"

# i的demo3
cloudServiceUrl: undefined
domain: "web-001.cloud.servicewechat.com"
expiresTs: 1657337060826
http: true
ip: undefined
key: "q4zmRdeEVKhZBPD+Olw2ZA=="
timestamp: 1657335260124
token: "58_cYSXYf_VVsubR0qkXlEd2v1y_zGj6dNsePLV8KeKNhKpHI4zPJYDgFZ6ovnJr6Jcf97jkDmYQVrGTqt-"
url: "https://web-001.cloud.servicewechat.com/wxa-qbase/container_service?token=58_cYSXYf_VVsubR0qkXlEd2v1y_zGj6dNsePLV8KeKNhKpHI4zPJYDgFZ6ovnJr6Jcf97jkDmYQVrGTqt-"
vip: "109.244.145.199"


# N的来源，依赖b
var R = r(44), N = R.compress(b);#25967行

# b的出处，依赖o
b = new Uint8Array(s.stringToArrayBuffer(JSON.stringify({
                                    method: c.method || "GET",
                                    header: O,
                                    body: v,  #"undefined"
                                    call_id: g
                                })))
                                
# o的出处，依赖y                            
for (var I in y)
    void 0 !== y[I] && null !== y[I] && O.push({
        key: I.toLowerCase(),
        value: y[I] + ""
    });            
# y的出处，
y = n.__assign(n.__assign({}, c.header), {
    "X-WX-ENV": e.isInstance ? e.env : (null === (h = c.config) || void 0 === h ? void 0 : h.env) || e.env,
    "X-WX-CALL-ID": g
});    

# y的demo1值
Accept-Language: "zh-CN"
HOST: "api-h5-tgw.ibox.art"
IB-DEVICE-ID: "9ad7fdb73e434a8faf339a1e6298a0ca"
IB-PLATFORM-TYPE: "web"
IB-TRANS-ID: "b4d0ea1ed6ef4ae181fa51211a64859c"  # todo syj
User-Agent: ""
X-WX-CALL-ID: "0.6121920070126474_1657332318464" # todo syj
X-WX-CONTAINER-PATH: "/nft-mall-web/v1.2/nft/product/getResellList?type=0&origin=0&sort=0&page=1&pageSize=50"
X-WX-ENV: "ibox-3gldlr1u1a8322d4"
X-WX-EXCLUDE-CREDENTIALS: "unionid, cloudbase-access-token, openid"
X-WX-GATEWAY-ID: "gw-1-1g2n1gd143d56b56"  # tod syj
X-WX-REGION: "ap-beijing"
X-WX-RESOURCE-APPID: "wxe77e91c2fdb64e85"
content-type: "application/json"    

# y的demo2值
Accept-Language: "zh-CN"
HOST: "api-h5-tgw.ibox.art"
IB-DEVICE-ID: "9ad7fdb73e434a8faf339a1e6298a0ca"
IB-PLATFORM-TYPE: "web"
IB-TRANS-ID: "72d744d037dd413888f31841e2edd642"
User-Agent: ""
X-WX-CALL-ID: "0.8205257333610667_1657333326859"
X-WX-CONTAINER-PATH: "/nft-mall-web/v1.2/nft/product/getResellList?type=0&origin=0&sort=0&page=1&pageSize=50"
X-WX-ENV: "ibox-3gldlr1u1a8322d4"
X-WX-EXCLUDE-CREDENTIALS: "unionid, cloudbase-access-token, openid"
X-WX-GATEWAY-ID: "gw-1-1g2n1gd143d56b56"
X-WX-REGION: "ap-beijing"
X-WX-RESOURCE-APPID: "wxe77e91c2fdb64e85"
content-type: "application/json"

# call-id的值，依赖g
g = Math.random() + "_" + Date.now()           
'''
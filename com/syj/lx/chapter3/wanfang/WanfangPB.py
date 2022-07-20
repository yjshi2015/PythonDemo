import request_pb2 as pb
import httpx

search_request = pb.SearchService.SearchRequest()

search_sort = pb.SearchService.SearchSort()
search_sort.field = ""
search_sort.order = 1

second = pb.SearchService.Second()
second.field = ""
second.value = ""

search_request.commonRequest.searchType = "paper"
search_request.commonRequest.searchWord = "哔站"
# search_request.commonRequest.searchSort = search_sort
search_request.commonRequest.secondsList.append(second)
search_request.commonRequest.currentPage = 1
search_request.commonRequest.pageSize = 5
search_request.commonRequest.searchScope = 0
search_request.commonRequest.searchFilterList.append(0)
bytes_body = search_request.SerializeToString()
print(bytes_body.decode())
bytes_head = bytes([0, 0, 0, 0, len(bytes_body)])
# 此处逻辑参考deal_request.js中第57行开始的代码
data = bytes_head + bytes_body

headers = {
    'accept': "*/*",
    'accept-encodind': "gzip, deflate, br",
    'accept-language': "zh-CN,zh;q=0.9",
    'cache-control': "no-cache",
    'content-length': "31",
    'content-type': "application/grpc-web+proto",
    'cookie': "_pk_id.30002.2c81=5a3cc07b733f5e39.1658148341.; Hm_lvt_838fbc4154ad87515435bf1e10023fab=1658148341,1658273605; zh_choose=n; firstvisit_backurl=http%3A//www.wanfangdata.com.cn; _pk_ref.30002.2c81=%5B%22%22%2C%22%22%2C1658276111%2C%22https%3A%2F%2Fwww.wanfangdata.com.cn%2F%22%5D; _pk_ses.30002.2c81=1; Hm_lpvt_838fbc4154ad87515435bf1e10023fab=1658276537",
    'cookies': "CASTGC=;CASTGCSpecial=;",
    'origin': "http://s.wanfangdata.com.cn",
    'pragma': "no-cache",
    'referer': "http://s.wanfangdata.com.cn/paper?q=%E5%93%94%E7%AB%99",
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': "?0",
    'sec-ch-ua-platform': "Windows",
    'sec-fetch-dest': "empty",
    'sec-fetch-mode': "cors",
    'sec-fetch-site': "same-origin",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    'x-grpc-web': "1",
    'x-user-agent': "grpc-web-javascript/0.1"
}

url = 'https://s.wanfangdata.com.cn/SearchService.SearchService/search'
with httpx.Client(http2=True) as client:
    response = client.post(url, data=data, headers=headers)
    print(response.content)

# response = requests.post(url=url, data=bytes_head+bytes_body, headers=headers)
# print(response.content)
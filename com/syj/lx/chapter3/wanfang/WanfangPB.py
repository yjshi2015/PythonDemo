import request_pb2 as pb

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
print(bytes_body)
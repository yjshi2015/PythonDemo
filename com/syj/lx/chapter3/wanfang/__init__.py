'''
PB使用步骤
①下载protoc.exe文件，地址：https://github.com/protocolbuffers/protobuf/releases
②配置环境变量，protoc_path，值为protoc.exe所在的路径
③安装protobuf的python包，pip3 install protobuf
④执行编译proto文件(在protoc文件对应的目录下执行如下命令）
.\protoc.exe --python_out=$DST_DIR $SRC_DIR/your.proto
$DST_DIR 为编译后的路径
$SRC_DIR 为proto文件的路径

'''



pb = '''
proto.SearchService.CommonRequest.toObject = function(e, t) {
    var a, s = {
        searchType: r.Message.getFieldWithDefault(t, 1, ""),
        searchWord: r.Message.getFieldWithDefault(t, 2, ""),
        searchSort: (a = t.getSearchSort()) && proto.SearchService.SearchSort.toObject(e, a),
        secondsList: r.Message.toObjectList(t.getSecondsList(), proto.SearchService.Second.toObject, e),
        currentPage: r.Message.getFieldWithDefault(t, 5, 0),
        pageSize: r.Message.getFieldWithDefault(t, 6, 0),
        searchScope: r.Message.getFieldWithDefault(t, 7, 0),
        searchFilterList: r.Message.getField(t, 8),
        languageExpand: r.Message.getFieldWithDefault(t, 9, !1),
        topicExpand: r.Message.getFieldWithDefault(t, 10, !1)
    };
    return e && (s.$jspbMessageInstance = t),
    s
}

proto.SearchService.CommonRequest.serializeBinaryToWriter = function(e, t) {
    var a = void 0;
    a = e.getSearchType();
    a.length > 0 && t.writeString(1, a);
    a = e.getSearchWord();
    a.length > 0 && t.writeString(2, a);
    a = e.getSearchSort();
    null != a && t.writeMessage(3, a, proto.SearchService.SearchSort.serializeBinaryToWriter);
    a = e.getSecondsList();
    a.length > 0 && t.writeRepeatedMessage(4, a, proto.SearchService.Second.serializeBinaryToWriter);
    a = e.getCurrentPage();
    0 !== a && t.writeInt32(5, a);
    a = e.getPageSize();
    0 !== a && t.writeInt32(6, a);
    a = e.getSearchScope();
    0 !== a && t.writeEnum(7, a);
    a = e.getSearchFilterList();
    a.length > 0 && t.writePackedEnum(8, a);
    a = e.getLanguageExpand();
    a && t.writeBool(9, a);
    a = e.getTopicExpand();
    a && t.writeBool(10, a);
}
proto.SearchService.SearchSort.serializeBinaryToWriter = function(e, t) {
    var a = void 0;
    a = e.getField(),
    a.length > 0 && t.writeString(1, a),
    a = e.getOrder(),
    0 !== a && t.writeEnum(2, a)
}
proto.com.wanfangdata.search.Sort.Order = {
    ASC: 0,
    DESC: 1
},        
proto.SearchService.Second.serializeBinaryToWriter = function(e, t) {
    var a = void 0;
    a = e.getField(),
    a.length > 0 && t.writeString(1, a),
    a = e.getValue(),
    a.length > 0 && t.writeString(2, a)
}   
    
    var t = mt.commonRequest
    , a = mt.searchRequest
    , r = mt.searchSort
    , s = mt.second
    , i = mt.scope
    , o = mt.filter
'''
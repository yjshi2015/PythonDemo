/*
    因为PhantomJS允许检测网络流量,因此它适合分析网络行为和性能,实现对网络的监听

    鉴于输出的内容较多,可以通过 phantomjs netmonitor.js >log.text 方式保存输出内容
*/

var url = 'http://movie.mtime.com/260270/';
var page = require('webpage').create();
// 通过onResourceRequest方法嗅探所有的资源请求
page.onResourceRequestd = function(request) {
    console.log('Request ' + JSON.stringify(request, undefined, 4));
};
// 通过onResourceReceived方法嗅探所有的资源响应
page.onResourceReceived = function(response) {
    console.log('Receive ' + JSON.stringify(response, undefined, 4));
};
page.open(url);
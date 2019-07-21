/*
    评估网页中的JavaScript代码,可以利用evaluate.这个执行是"沙盒模式"的,也就是安全模式的,
    它不会执行网页外的JavaScript代码
*/

var url = 'http://movie.mtime.com/260270/';
var page = require('webpage').create();
/*
    任何来自网页并且包括来自evaluate()内部代码的控制台信息,默认不会显示,覆盖此行为.
    通过coConsoleMessage回调方法
*/
page.onConsoleMessage = function(msg) {
    console.log('Page title is ' + msg);
}
page.open(url, function(status) {
    page.evaluate(function() {
        console.log('-------->evaluate:' + document.title);
    });
    phantom.exit();
});
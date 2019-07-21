// 加载页面并截图保存
var page = require('webpage').create();
page.open('http://movie.mtime.com/260270/', function(status) {
    console.log("status:" + status);
    if(status === "success") {
        page.render("syj.jpg")
    }
    phantom.exit()
})
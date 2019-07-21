// fs模块,即File System,主要是对文件系统进行操作

var fs = require('fs');
// 判断文件是否存在
var path = '/home/syj/IdeaProjects/PythonDemo/com/syj/demo/phantomJS/log.text';
if (fs.exists(path)) {
    console.log(path + ' exists.');
    // 读文件
    var content = fs.read(path);
    console.log('read data ', content);
} else {
    console.log(path + ' does not exist');
}


phantom.exit();
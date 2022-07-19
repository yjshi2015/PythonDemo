'''
在JS中，websocket的new WebSocket()是固定的语法，可以用作我们定位的关键词。
webSocket.send 用于向服务器发送数据
webSocket.onopen 用于指定连接成功后的回调函数
webSocket.onmessage 用于指定收到服务器数据后的回调函数
webSocket.onclose 用于指定连接关闭后的回调函数
webSocket.binaryType='arraybuffer'用来标识通用的、固定长度的原始二进制数据缓冲区

RPC最重要的是找到入口点，一般webSocket消息处理函数为onmessage 或者 addEventListener("message")

ws.onmessage = function(event) {
    var data = envent.data;
}

ws.addEventListener("message", function(event) {
    var data = event.data;
})
'''
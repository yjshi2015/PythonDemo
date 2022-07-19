import asyncio
import websockets


js = '''
window.dataSyj = r;
!function() {
    var res = window.dataSyj;
    if (window.flagSYJ) {
        window.wsSYJ.send(JSON.stringify(res));
    } else {
        var ws = new WebSocket("ws://127.0.0.1:9999");
        window.wsSYJ = ws;
        window.flagSYJ = true;
        ws.open = function(evt) {};
        ws.onmessage = function(evt) {
            ws.send(JSON.stringify(res))
        }
    }
}();
'''

async def check_permit(webSocket):
    send_text = 'syj'
    await webSocket.send(send_text)
    return True

async def recv_msg(webSocket):
    while 1:
        recv_text = await webSocket.recv()
        print(recv_text)

async def main_logic(webSocket, path):
    await check_permit(webSocket)
    await recv_msg(webSocket)

start_server = websockets.serve(main_logic, '127.0.0.1', 9999)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

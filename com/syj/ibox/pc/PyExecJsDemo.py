import execjs

print(execjs.get().name)

js_method = '''
var y = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";

function base64ToArrayBufferMock(e) {
    for (var t = function(e) {
        var t = String(e).replace(/=+$/, "")
            , r = "";
        if (t.length % 4 == 1)
            throw new Error('"atob" failed');
        for (var n = 0, i = void 0, o = void 0, a = 0;
             o = t.charAt(a++);
             ~o && (i = n % 4 ? 64 * i + o : o, n++ % 4) ? r += String.fromCharCode(255 & i >> (-2 * n & 6)) : 0)
            o = y.indexOf(o);
        return r
    }(e), r = t.length, n = new Uint8Array(r), i = 0; i < r; i++)
        n[i] = t.charCodeAt(i);
        console.log(n[i])
    return n
}

function ib_id(){
    const t = []
      , e = "0123456789abcdef";
    for (let n = 0; n < 36; n++)
        t[n] = e.substr(Math.floor(16 * Math.random()), 1);
    return t[14] = "4",
    t[19] = e.substr(3 & t[19] | 8, 1),
    t[8] = t[13] = t[18] = t[23] = "",
    t.join("")
}
'''
loader = execjs.compile(js_method)


def get_bytes(secret_key):
    result = loader.call('base64ToArrayBufferMock', secret_key)
    arr = []
    for k, v in result.items():
        arr.append(v)
    secret_key_bytes = bytes(arr)
    return secret_key_bytes


def get_trans_id():
    return loader.call('ib_id', '')


if __name__ == '__main__':
    result = get_bytes("zkXsdQURgkDefISbA6prjw==")
    print(result)

    trans_id = get_trans_id()
    print('llllllll', trans_id)

function nn(t, e, n) {
    var r = e.getMethodDescriptor()
        , o = n + r.name;
    n = new Te,
        n.H = t.c;
    var i = new Xe({
        T: n
    });
    if (i.l = r.b,
        we(n.headers, e.getMetadata()),
        "text" == t.a ? (n.headers.set("Content-Type", "application/grpc-web-text"),
            n.headers.set("Accept", "application/grpc-web-text")) : n.headers.set("Content-Type", "application/grpc-web+proto"),
        n.headers.set("X-User-Agent", "grpc-web-javascript/0.1"),
        n.headers.set("X-Grpc-Web", "1"),
        xe(n.headers.b, "deadline")) {
        var a = n.headers.get("deadline");
        a = Math.round(a - (new Date).getTime());
        var s = n.headers;
        xe(s.b, "deadline") && (delete s.b.deadline,
            s.c--,
        s.a.length > 2 * s.c && _e(s)),
        1 / 0 === a && (a = 0),
        0 < a && n.headers.set("grpc-timeout", a + "m")
    }
    if (t.f) {
        s = n.headers,
            _e(s),
            a = {};
        for (var u = 0; u < s.a.length; u++) {
            var c = s.a[u];
            a[c] = s.b[c]
        }
        s = n.headers,
            s.b = {},
            s.a.length = 0,
            s.c = 0;
        t: {
            for (l in a) {
                var l = !1;
                break t
            }
            l = !0
        }
        l || (a = tn(a),
            "string" === typeof o ? (l = encodeURIComponent("$httpHeaders"),
                a = null != a ? "=" + encodeURIComponent(String(a)) : "",
            (l += a) && (a = o.indexOf("#"),
            0 > a && (a = o.length),
                s = o.indexOf("?"),
                0 > s || s > a ? (s = a,
                    u = "") : u = o.substring(s + 1, a),
                o = [o.substr(0, s), u, o.substr(a)],
                a = o[1],
                o[1] = l ? a ? a + "&" + l : l : a,
                o = o[0] + (o[1] ? "?" + o[1] : "") + o[2])) : o.a("$httpHeaders", a))
    }
    for (e = (0,
        r.a)(e.getRequestMessage()),
             r = e.length,
             l = [0, 0, 0, 0],
             a = new Uint8Array(5 + r),  // ①初始化一个空字节数组，长度增加5个字节
             s = 3; 0 <= s; s--)
        l[s] = r % 256,  //②这里先给后4个字节赋值，其中l[3]为e的长度，l[0~2]为0
            r >>>= 8;
    if (a.set(new Uint8Array(l), 1), //③从下标1开始，把l字节数组的值赋给变量a
        a.set(e, 5), //④从下标5开始，把e字节组的值赋给变量a
        e = a, //⑤a变量构造完成，赋值e
    "text" == t.a) {
        var f;
        for (t = e,
             void 0 === f && (f = 0),
                 qe(),
                 f = He[f],
                 e = [],
                 r = 0; r < t.length; r += 3) {
            c = t[r];
            var d = (l = r + 1 < t.length) ? t[r + 1] : 0;
            u = (a = r + 2 < t.length) ? t[r + 2] : 0,
                s = c >> 2,
                c = (3 & c) << 4 | d >> 4,
                d = (15 & d) << 2 | u >> 6,
                u &= 63,
            a || (u = 64,
            l || (d = 64)),
                e.push(f[s], f[c], f[d] || "", f[u] || "")
        }
        e = e.join("")
    } else
        "binary" == t.a && (n.j = "arraybuffer");
    return Me(n, o, e),
        i
}
# 百度网站登录加密分析

1.通过对登录环节进行Firebug,发现输入完密码点击**登录**后有一次重要的POST请求,具体如下
  URL:      https://passport.baidu.com/v2/api/?login
  request:  
            staticpage	https://www.baidu.com/cache/user/html/v3Jump.html
            charset	UTF-8
            token	ae8ac14cc81d43e6f8a16798a3bf4d3a
            tpl	mn
            subpro	
            apiver	v3
            tt	1564442081172
            codestring	
            safeflg	0
            u	https://www.baidu.com/
            isPhone	false
            detect	1
            gid	6DFCC73-D941-4383-BDEF-F7C7E24CA9CC
            quick_user	0
            logintype	dialogLogin
            logLoginType	pc_loginDialog
            idc	
            loginmerge	true
            splogin	rate
            username	Far_Away0903
            password	Dh0Ux9qriUNA29HzBJcDr8b3VDIgVIricZF0Ikd5BEzFonSE17HRU0beLJrwRIhZVK6LQZXLa5VDvAz3knI8Df/DZXWxVel8cqbI8RLOzadsetmfw5RMxEuDVvfRWcDWxtRQ1zyHfFMQzxjKrTGeIIWM3F+UhNkGaBsJMepYqWE=
            mem_pass	on
            rsakey	gYak0M53IICsBcHnP92y2x6p53fjfJrR
            crypttype	12
            ppui_logintime	32899
            countrycode	
            fp_uid	
            fp_info	
            loginversion	v4
            ds	lG80iqH9it8NeTvwspAFwFLIAG7STmMhf+Xi2qVCpJWdRWQ0IgfIBPtNX6zHUHjF4foPcJ+OsU/4WlWBc1Oau7PLal4j7hwNB9+RzY4vA+Z+0R9CGObxCG5veSlLWY/lrVCMy9RJAjHN9VYKY9WUMj79kScJ7NUC0klcdQjvXqML2T6YByxcwJlz7to2g1K39MGTL2+fSbINY4qw9GVoDmSa7v67SGVZEOvPzsayWnEHmZ+8fGeEbGShWi4454AGrlRLptRll993romDFvHGsvbfZW6xHQ+8Q55r9SGjaKsTNRUGV3xLOSEhKobnK739Pyl1ijEykjK13NBnS67knpcV007EK6AD5ycUHXasuNmdWrpbgVbf4aeAFbMi8EtO2vIkPr3ptxOQ4LWQgFhb+IDweGk5tymLNVHr+YCohdwiCkDmL6cxcTKZ3FGK8KjzMtHLNDnGPoIG3aIk75wyn7Ge+JHKmyN5CsmF8YaB+gK8+pQWHh3dNhxY5FwqEdw36U3fWKGUnSbjTg3r9OfP2dsfyRJSLGtSAgLUsXCSFpOGGP8WZsBq/y8jxGwjihdiiPYvST3S4dB2iCEwo20ntKHnL5ndnUi8/yc9pTrZv+MKGu2LGITvI1Ff5si/bIP0JvhW9Va+udVCoIrGr7+tG0LgwRVUBNTJJSDrSEjBgiTivKbNChpxq3NNh0CaYJq67Fl2mqC7iiHqKVPe+ydgJ2PwtllNPn0h795x3gO2vdOAQcb24XxLWWU5OPiZ++FaNxLKRIfIAnR9DYS91O0+FbaPtgwbrfR4Z+4SwY5r97l4jLsWE/UlDdBanMeKRroWvcU42fQNLPi6hdwzqU+WC/pYs2oyRDHe3oEghc3vcvXva8sJMSb+1yR+n1sn7pLxyEwqo+x2rV9PpOZwM0GyQ1wmHqj1+n5yF/4lVp92+qk=
            tk	3618JUop/gPamhRglEivRMnwDE6NmLbsWYLnZyvr1Xc43WfVLp4Nuv3hVBvdRWTnTOU830u8c4oeoPNvE8eragE2GA==
            dv	tk0.4954741985374361564442049957@sri0fs6AWg5kuguXwguAD~uXgwNM6Z5MhVOjIH2MRcOrya2GzL6AWz5kBX5k0j63tj5vEhAWSs9D-FM-hADvLguvyFBrvZB~SeBUEL6A9j5k0~umwXpAWlpsgD9Dz4DWv6M-y9D-hFuAhFM~6-NU-dS4w_-vv2uvBh~~8ShBiguQwZ5kNlEiMSrCw539z6A9~6k0zpkDZ6Z9Z630-639x6ktw6kWz6AB_giM24ExB4uf5Xy~S~BHNUvdo4DHNjyc5Xg-OUEToUTHoG9_HitpARC63DCuAtzuswXuABCuAuj6Qw~63RCuAuwuswguZqg5kBx6q__
            fuid	FOCoIC3q5fKa8fgJnwzbE+YhNskVRU4HW930FeLFkOAnC0nPCMRDCWKSQrJ7O1YBbapN5lVGCJM4DzCe77kSPhL2uITGd6it5WO+NY2vJfGuXjUjgAqxRZTedGmkLl0usJSd6F3RV2tSAGCgUnxdNh5p0wcNk5rJBw2ph9fw2fuA5W5aWyRLiOlolyCGVS7qB1dYQJBVRgdi1KHBJ+Xl2UJeDHUs3GBB97C3qgUKwapVEoJ+QFRuKHbRqMpKP64xW8WivYeq15EPbJBsd8pf0uNzmz9vDqhv6LGpSWzcyGR8lSS9cqxXHMd/VQ4vnO3SFeLs4wygIv6m069lhsdmzWfcAPqEz2JquN2pkeuE7++IGhYqrYfhHGZqJNx2uWmglAIQEZY21OyYDgpfKN3zxZGnFOqvdQfOKZU4zWdx+C1LbkcRFSwgx9I2WcAjRLAxi6L0BPA661JDj0lmZIgcCFL8aJ0hktpYIjWQcYCvzWnej97H78r2IclzcMZuksx/…aSs0GhPBe+LI0RU4jdx13gvFC6q1wCULJ4C7lqWgAolJ4djuZOvDBJIoLdlon+K8ez0EEYov1s4bOPFeaoPMIggScGW0ZK1omM5t9hyC1z4PHoQmeZwiGX72aWxKBActEFfVtxkA272i7VrJ6Mtrt6U81JZT2lI/BqZAlQtfbSsfWbASoYJvrHtmWN3mR1t60LRtCcipUb2J/sZLe+E6qnOipQbkzjeYHexVCW6Yjob/LCg07Am/TvhwTKYNYHeDpCtd6RMvOgbCfDNICl4LYr1IDPAY5dZv6ZINErg8p7Vi3a5jMXGWL4Mkr0ksENkLZvBJChyDMkf14Hx56V+b2nRqUTK6NqmhPLvsfMNYCRyESom9rukNSbUImRNUXXv70cfMSn4OrmEd+59Ab34CROfim3rsAsgLyURlANn6bdFQpSH1dJtj0Ru27x9NDjgymOnBYuzYFgCuiXNRuHzXA4oSp6fFDSjcO2f21jnCARd+2gYcoj1jwDnmFwagA==
            traceid	73B5AB01
            callback	parent.bd__pcbs__pgylit
  response: 响应为一个页面

2. 通过对多次登录的post请求分析,发现如下参数是动态变化(其他不变):
   tt
   gid
   token
   password
   rsakey
   ppui_logintime
   ds
   tk
   dv
   fuid
   traceid
   callback

3. `tt`为时间变量,暂时可忽略
   `gid` 在FireBug的**调试器**中,通过Ctrl + shift + F 全局搜gid,发现在https://passport.bdimg.com/passApi/js/loginv4_2857b87.js文件中存在
         git的计算逻辑,如下
         ```
          '&overseas=' + t.config.overseas + '&gid=' + t.guideRandom 
           省略无数
         this.guideRandom = function () {
         return 'xxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (e) {
         var t = 16 * Math.random() | 0,
         n = 'x' === e ? t : 3 & t | 8;
         return n.toString(16)
         }).toUpperCase()
         }(),
         ```
   `token`在如下请求中作为返回值被发现
        url:https://passport.baidu.com/v2/api/?getapi&tpl=mn&apiver=v3&tt=1564442048271&class=login&gid=6DFCC73-D941-4383-BDEF-F7C7E24CA9CC&loginversion=v4&logintype=dialogLogin&traceid=&callback=bd__cbs__8mxvd0
        request:
           getapi	
           tpl	mn
           apiver	v3
           tt	1564442048271
           class	login
           gid	6DFCC73-D941-4383-BDEF-F7C7E24CA9CC
           loginversion	v4
           logintype	dialogLogin
           traceid	
           callback	bd__cbs__8mxvd0
        response:
           bd__cbs__8mxvd0({"errInfo":{        "no": "0"    },    "data": {        "rememberedUserName" : "",        "codeString" : "",        "token" : "ae8ac14cc81d43e6f8a16798a3bf4d3a",        "cookie" : "1",        "usernametype":"",        "spLogin" : "rate",        "disable":"",        "loginrecord":{            'email':[            ],            'phone':[            ]        }    },    "traceid": ""})
   `rsakey`在POST请求之前不远处,有一个请求的响应中发现了rsakey的值,只不过属性名称变为了key,但可以断定,这个就是raskey的生成方式
        url:https://passport.baidu.com/v2/getpublickey?token=ae8ac14cc81d43e6f8a16798a3bf4d3a&tpl=mn&apiver=v3&tt=1564442064953&gid=6DFCC73-D941-4383-BDEF-F7C7E24CA9CC&loginversion=v4&traceid=&callback=bd__cbs__qu1gy0
        request:
           token	ae8ac14cc81d43e6f8a16798a3bf4d3a
           tpl	mn
           apiver	v3
           tt	1564442064953
           gid	6DFCC73-D941-4383-BDEF-F7C7E24CA9CC
           loginversion	v4
           traceid	
           callback	bd__cbs__qu1gy0
        response:
           bd__cbs__qu1gy0({"errno":'0',"msg":'',"pubkey":'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCckwQuuo2OrrarRfLvI8rNpp8y\nHLvs1TSz\/oIbo1wZklhjw1DAYyF\/AlrG3jn6GYwMngDsH05NGnJCgCMSe5o3D04R\nvTgH\/hl+yNzI5O1IE3yHmBLjKJFcrcs33IYnA6NOg4RigPhgkzXbY8WsbifbU\/42\njsTErlD2RJG6nNMJVQIDAQAB\n-----END PUBLIC KEY-----\n',"key":'gYak0M53IICsBcHnP92y2x6p53fjfJrR',    "traceid": ""})   
        结论:rsakey是由gid和token生成的,并且密码是通过RSA加密的,响应中的publickey是公钥!!!
   `ppui_logintime` 在**调试器**搜索该关键词,然后在https://passport.bdimg.com/passApi/js/loginv4_2857b87.js中发现一系列下列内容
        ```
        login: {
        memberPass: 'mem_pass',
        safeFlag: 'safeflg',
        isPhone: 'isPhone',
        timeSpan: 'ppui_logintime',
        logLoginType: 'logLoginType'
        },
        o.timeSpan = (new Date).getTime() - e.initTime,
        t.initTime = (new Date).getTime(),
        ```
        可以断定这是一个判断这是一个从输入登录信息,一直到点击登录按钮提交的这段时间,故用之前的值也行
   `callback` 在**调试器**搜索callback,一无所获,搜索bd__pcbs__发现如下脚本,可以猜测这既是callback的生成逻辑
        ```
        u = c.getUniqueId('bd__pcbs__');
        t[r.queryField || 'callback'] = 'parent.' + u;
        e.getUniqueId = function (e) {
        return e + Math.floor(2147483648 * Math.random()).toString(36)
        },
        ```
   `passport` 在**调试器**中搜索passport,发现如下脚本,可认为是密码的生成逻辑,对password通过公钥pubkey对密码进行加密,最后对输
        出进行base64编码,即为最后的加密密码(虽然我没看明白)
        ```
        var r = e._SBCtoDBC(e.getElement('password').value);
        if (e.RSA && e.rsakey) {
        var a = r;
        a.length < 128 && !e.config.safeFlag && (o.password = baidu.url.escapeSymbol(e.RSA.encrypt(a)), o.rsakey = e.rsakey, o.crypttype = 12)
        }
        ```
   `traceId` 在**网络请求**的post之前,并未找到含有traceId的请求,故判定是在前台js中产生而非后台服务端产生,在**调试器**中全局搜
        traceId,发现有如下逻辑,总之也是跟时间相关的,因此用之前的traceID也是可以的
        ```
        createTraceID: function () {
        var e = this;
        return e.headID + e.flowID + e.cases
        },
        initTraceID: function (e) {
        var t = this;
        e && e.length > 0 ? (t.headID = e.slice(0, 6), t.flowID = e.slice(6, 8))  : t.destory()
        },
        getRandom: function () {
        return parseInt(90 * Math.random() + 10, 10)
        },
        createHeadID: function () {
        var e = this,
        t = (new Date).getTime() + e.getRandom().toString(),
        n = Number(t).toString(16),
        i = n.length,
        s = n.slice(i - 6, i).toUpperCase();
        e.headID = s
        },
        getTraceID: function (e) {
        var t = this,
        n = e && e.traceid || '';
        t.initTraceID(n)
        },
        getFlowID: function (e) {
        var t = {
        login: '01',
        reg: '02'
        };
        return t[e]
        },
        ```
   `ds/tk` 在**核心POST请求**前附近处,发现如下GET请求,故需要追溯`ak/as/fs/callback/v`的来源,mygod!!!

        url:https://passport.baidu.com/viewlog?ak=1e3f2dd1c81f2075171a547893391274&as=65ce3ff4&fs=p6%2BgRB2AHghmigewrfBvCZGc1ky%2FpXz6U%2FI7URpWHxy8y%2FbLpEEyOlFryorre8KiOw4CRwKb99RYsTXRrsIMfcwckdHurRQ4K8re6DK9XJSqg2vf77CZYUx5tcSbSD%2BIIgI2yDBg5VWtzp%2Bnh1f4X1gp81EEBttzhil%2Bs%2F87goc16JNvHci5PutTMKylVLnYpzrYNHhyj81dbLpNgWsms5QCZDAxpL3ajJXLgfI78ubqejfXrIVvwSUTfsek%2BB%2F90mxJCZ3ekLOxcY7gYlUZtEf26wPAzGB%2BDIGZMXXfBj2ePpu3b0XKgyUv%2B%2BQqXCh2R9LfEBxwvzRdG0bp4oYLXU0pMWASyFE4gt9Fy%2B87FcKfdjWPb6jn6SmYrKgBbMgQGxwc4T35vINThZ%2FWmqy843W7GMfM0B6Cz3C9tvkqpOJRfnPFwh%2BkYo%2FDQTMdzyEpK%2BbcAgx9dj1S%2FYIAgcSW8w2%2BhiXsJxWlRfkRavtWYX6kj0RUps%2Bb6C%2FvptiZvtrR8P%2Ban%2B%2Fa9tdvFiWEh9UEKfPa6LKmPNAUsngzn48GEC9416irL3etPj3Qu6M50ulcs3yvSR2c3QGpWqMtjoK3L24j%2BapIB6fdn80dk%2Bsf4evyn%2BV5v02%2BovhBTbRQt5Ka%2FrnFRvFRZXrbnctIjghxZ7z5Ppir8X22tiQqiT0VKx%2BFbgUSrN0rRXpJsdr7LKYDx50S97ZecEILRJ7zJnqwPL2k%2BCU5PiOnm%2FDche1SbQIoWIoUNBJgbxySs4LWWvOUwDZJCwWJ4sZpuS8s5lIn5VNFNhSK%2FVFw2TPEhaKWVDTPKQ9yYVvqkUncd28aoH1c&callback=jsonpCallbackb5621&v=5089
        request:
            ak	1e3f2dd1c81f2075171a547893391274
            as	65ce3ff4
            fs	p6 gRB2AHghmigewrfBvCZGc1ky/pXz6U/I7URpWHxy8y/bLpEEyOlFryorre8KiOw4CRwKb99RYsTXRrsIMfcwckdHurRQ4K8re6DK9XJSqg2vf77CZYUx5tcSbSD IIgI2yDBg5VWtzp nh1f4X1gp81EEBttzhil s/87goc16JNvHci5PutTMKylVLnYpzrYNHhyj81dbLpNgWsms5QCZDAxpL3ajJXLgfI78ubqejfXrIVvwSUTfsek B/90mxJCZ3ekLOxcY7gYlUZtEf26wPAzGB DIGZMXXfBj2ePpu3b0XKgyUv QqXCh2R9LfEBxwvzRdG0bp4oYLXU0pMWASyFE4gt9Fy 87FcKfdjWPb6jn6SmYrKgBbMgQGxwc4T35vINThZ/Wmqy843W7GMfM0B6Cz3C9tvkqpOJRfnPFwh kYo/DQTMdzyEpK bcAgx9dj1S/YIAgcSW8w2 hiXsJxWlRfkRavtWYX6kj0RUps b6C/vptiZvtrR8P an /a9tdvFiWEh9UEKfPa6LKmPNAUsngzn48GEC9416irL3etPj3Qu6M50ulcs3yvSR2c3QGpWqMtjoK3L24j apIB6fdn80dk sf4evyn V5v02 ovhBTbRQt5Ka/rnFRvFRZXrbnctIjghxZ7z5Ppir8X22tiQqiT0VKx FbgUSrN0rRXpJsdr7LKYDx50S97ZecEILRJ7zJnqwPL2k CU5PiOnm/Dche1SbQIoWIoUNBJgbxySs4LWWvOUwDZJCwWJ4sZpuS8s5lIn5VNFNhSK/VFw2TPEhaKWVDTPKQ9yYVvqkUncd28aoH1c
            callback	jsonpCallbackb5621
            v	5089
        response:
            tk	6512R9hoFakIvPLtWe3FQUdnThEnV0IHBx25neiXhr4XbrCPxhFDQwqAQGjLoqIa+KySskW7kOQtBghwSwIGEoDyNw==
            as	65ce3ff4
            ds	pPewyKpZ/srbBZqcvH0ErmnHk9drEOMndzncwXR7ieM5LvSryJsdTnPvE7WpNtLM+MNQxQr716TJwGOHLpj79iH0VSt8OldaS2DcdpXUjTz4/MXdN3pF8Fuj5ncnhzVoXVdowfu0UTgCemchvslqnKMKiUvGDukxyqVp45e2S/snOh3yE6Q16rQsFRVI4ZV3Afl0vxpkicw9Q653G1COyMBX3pyTmWLYVY88COm+iumcSBjppCcUo1pKWSDqU6/nDrt29IBZvQpWJG5+f6E0WqUrl1ey+kiyifPZexny6IN8xxYdMd8SriJSB/TZ9dpUY2VwU2ms/WQtenaTIt/9duQHIdY43YTf+wpXOeUWy0/LR94VRc/t/Gdd1LFl+KnteTo5QoCtSQaQV0qdmxECNrLJINVrd//eW3PIEwvfoP+BJYMacli659eBbHoPfZzk3jWVuyQVMbrKkGn27DOM1yoQ2W1/e2D7vspb2coJdgWddGoXCVXKp2zMEGoFXPRXTIXQltBrffOM/1RwseVoOQS9bNQ2nqae49zvbTV6RfuKm34Uz/N7bgo6lEsBpVnJzirX8OxeyZUVT3JNRuMX1KCMB9M+r+uFfk9RD4JB9w63geOKgIjwOu2B/toBPoTuRUYLZpZW+2L+lUe8NyjIxmWuJvEqB5IPsZI/YfXS/qR6DMy3uroDB/xTlvmp8fm0YEynVMSRoqcyAT6x+UESUwSdBqONjO9qxkszcP3fCxbXecV08p3ulhPgoYRFcajjSYKuik+A4YFJ/Wvav2y7DvbztMius73Rq0CcL8WOnXLjxFDDookoCFb0oGPF9w1fCAuqQCU9ILGISckGJZ+QTQ==
       
       
# JD网址加密登录分析
-1. 核心POST请求网址:	https://passport.jd.com/uc/loginService?uuid=4fee3d5c-765a-4fc0-98eb-23a615605ba2&ReturnUrl=http%3A%2F%2Fwww.jd.com%2F&r=0.27569211808468663&version=2015
    请求的cookie	
    __jda	122270672.15646146080041922484744.1564614608.1564614608.1564614608.1
    __jdb	122270672.6.15646146080041922484744|1.1564614608
    __jdc	122270672
    __jdu	15646146080041922484744
    __jdv	122270672|direct|-|none|-|1564614608006
    _t	wX+QAiySyPTG5HDjY0w8LJ0zk4I4bA1udYORjgNPN9k=
    3AB9D23F7A4B3C9B	EWI2DOAWYJLAEHNFREGSLKBHUY6P3GNQCJYYK7MLL457IA6R3UYTV3IYLC7D5JK2HGGJ4MHKZYRNLXT3WFSTYKIGDA
    alc	hj0d5A4c351HGtzZwNXAgA==
    wlfstk_smdl	zm6pjicxr32miftrfnvo0k2kuebpucwu 
    请求参数	
    uuid	4fee3d5c-765a-4fc0-98eb-23a615605ba2
    eid	EWI2DOAWYJLAEHNFREGSLKBHUY6P3GNQCJYYK7MLL457IA6R3UYTV3IYLC7D5JK2HGGJ4MHKZYRNLXT3WFSTYKIGDA
    fp	a0142140ed2fdf5087eef7f9244bb5fd
    _t	_t
    loginType	c
    loginname	18618224639
    nloginpwd	WjTK6PWtzI0F69vjU+JGjCgvYDX3rt6r6rUYloGX9jhX9K1BIGSZlrwncqnwXCyR9H3TaX96JAou/6g2JCuEPpyI3FtajE0chUln9TxT5wMYn+VAjOuWynNs4jcv/JwicitmtjZv6eO0Hzxzt04OQa/LkRRAungNriSTId8ZTNo=
    authcode	944d8a9da5ed440ab7d6ab08af051dd8
    pubKey	MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDC7kw8r6tq43pwApYvkJ5laljaN9BZb21TAIfT/vexbobzH7Q8SUdP5uDPXEBKzOjx2L28y7Xs1d9v3tdPfKI2LR7PAzWBmDMn8riHrDDNpUpJnlAGUqJG9ooPn8j7YNpcxCa1iybOlc2kEhmJn5uwoanQq+CA6agNkqly2H4j6wIDAQAB
    sa_token	B68C442BE645754F33277E70120805905E88F11B17C0C5B96C2EE9A9393C192F11831A68798734503EE8119A5D21F8A40F6ADF76CCAA41D80DA72772D66CCBBFEB74872621B17D025772F22D0DEE899FE4A6F233A7686A267CCEBCCAE692B1CB84BB33EE98450902633F508AD660A497CE419D5643EF2404D6B508587E92F6F14EEBB18883E297806C9A3C80D25A166AA64835D8E3B300A750B80B0F13C35DB178F376B1C00A0E963C5DFAB3D1758E4DA0E36BC8B94DE54C104F8E3AEA3BE33F52C9AB8056818012F8C78039C5E0143B5155E910DB9077BAE24249A74E8D14F23E811AA89E072694B5A5AB42322F1F7ED36739815BD82A47E3D4A02CE84B78486BCCAAF0DDD1D168B2BDAE1CF4E85476AFCC0D52DBF8363CBD0817E467E408C4DBA6D908AFDDD30EE92BC3FA5971D03ABAFCCAB7C4B35C1A9000FF2019C82662E754FD0264D909CE2C89C205C61F621CB20B255F973065733B7E0B7787B90F4A77F336CB8F2AC155B4BD79C7BC6AD1C711256C02208F66ED68ECCD5892DCC456431D21B7C7AE6C6AA4CD597A68307344
    seqSid	381015646146452900
    useSlideAuthCode	1
    
    `uuid` 在POST之前的所有网络请求的返回体中未找到,然后回归JS脚本,在疑似的存在,但加工逻辑跟实际得出的结果貌似不匹配,不了了之
    `eid` 在如下网络请求的返回体中发现,但该请求的入参无法定位,不了了之
    ```
    请求地址:https://gia.jd.com/fcf.html?a=7TJI7TceW0Pu7Tce7TZ37Tce7Tce7T7L7TcezlP47Tce7TZ37Tce7Tce7T7L7TceWIAewGAB6SAewdwPwHcPw4wPwH7QWIAewGAB6SAewQ%3C*wT6ewT6*Fg6eFQRQZT2DZlfPFHJQOTcjZ07GZgF47Tce7T7L7TceJGAewGAB6SAewHcuZIDxwIDx7Tce7T7L7TceFGAewGAB6SAewH%3CPwHcPw4wPwH7X7Tce7TZ37TceW0NBWt3XWd6uyQ6uil9C7T70zQft7T70z09dygDuihZ*qIAewGAe6eAewdNB7Tce7TZ37TceAQfjJh7ufh7s7TZ%3Cy1RjWIAeZTZ37Tckw4iPwHAeRdJtJeEUFIEHzljPwHAeRGAewGAe6eAewQFH7Tce7TZ37TceRfJ7w4R56fJFS4x3RAbORP7NRkZwSj7cff4lALZ1TPNLSPPFSBJZT%3C*jZTJ76TFSwkfFfNiBSfPw6BJ%3CZApvw4b1RjojTAbvgPPST4xifLZhRPZAgAC7RjR37Tce7T7L7TceJIAewGAB6SAewPZKZNJcwPWj6PZiTk7TTH7AAB7ZALijAAFy6kAefj7NRfRZZLRLRAf3g%3C9RfHfISAPTSAZfAfAkRTRggN73ZkpIgAxNRjPKgfN7wPaj7Tce7T7L7TceWg4PwHcPwj%3CPwHcPwHcPZj6/
    request body:
        g: 7TJI7TceJhZPW4NdFgEj7Tce7TZ37TceOTZGZHJPFg6eZg6tZQ7bZBcBwT4DiTJQO0wEFQF4wB4PwHcPw4wPwH7XWQPdygDPwHcPwj<PwH7*ieAewGAe6eAewQxbzQJkigJP7Tce7TZ37TceqQaC6jDPwHcPw4wPwH7XWeAewGAB6SAewQxpzdfD7Tce7T7L7TceztZgFh7Byg9u7Tce7TZ37TceT4<PwHcPw4wPwH7GWQ9tWlfe7Tce7TZ37TceRQPeFgFXqIAewGAe6eAewQ7eztJBFh7gFh7Byg9u7Tce7TZ37TceZHauwIAewGAe6eAewQZXz09eR0f*J0aPwHcPwj<eZIAe6eAewdZHWQfPzP7PWl9sJhRpzlDPwHcPwj<PwHctZHbDwTwlZGAewGAe6eAewdRpzgfmzlEPTlFQWlfj7Tce7TZ3vTaPw4wPwH7BFhZByg9uAtRXWQNdFSAewGAB6hReJgAPw4wPwH7szlZbzNZjzt7bFlAPwHcPwjNjWdfP7T7L7TceygE4FhbPF<RG7Tce7TZ3J17kFSAe6eAewQN4F<7Py0Nlyg9e7Tce7TZ3FQNsWlAPw4wPwH7XW0fuR0Njig7bWlAPwHcPwjNQigxBFSAe6eAewd3sihRQzt7C7Tce7TZ37TceT0PuJhaPwH3DOLFVZH6PwHcPw4wPwH7HilDPwHcPwj<j7T7L7TceihZe7Tce7TZ37TceZL6xwL2PwHcPw4wPwH7jWQNHyeAewGAB6SAewdfuWt3PilPQygf47Tce7T7L7TceW0xkFlPuWeAewGAB6SAewdfuF0fQygEPFIAewGAe6eAewQZbzdFbWeAewGAB6SAewH7GZHZbiHixwBPGZHWBigRbF0cBZl6*ZgR4F0FGwHWD7Tce7T7L7TceJlfGFl*PwHcPwj<PwHcBZH4kO0NGFH<EwBitig74ZL2*Zg6*ZT4DiBaEZT3HZSAewGAtR2/
    response body:
        EWI2DOAWYJLAEHNFREGSLKBHUY6P3GNQCJYYK7MLL457IA6R3UYTV3IYLC7D5JK2HGGJ4MHKZYRNLXT3WFSTYKIGDA    
    ```
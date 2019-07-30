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
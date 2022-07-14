import execjs

print(execjs.get().name)

file = 'cloud-sdk.js'
node = execjs.get()
ctx = node.compile(open(file, encoding='utf-8').read())

secret_key = "rw+is1wIDgoJAZvi65ow+A=="
js = f'base64ToArrayBufferMock1({secret_key})'
print(js)
result = ctx.eval(js)
print(result)
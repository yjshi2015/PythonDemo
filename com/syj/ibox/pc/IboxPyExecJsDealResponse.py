import execjs
print(execjs.get().name)


file = '../js/services.js'

# with open(file, encoding='utf-8') as f:
#     context = f.read()
#     position = context.find('0xa6')
#     print(context[position: position +1000])

ctx = execjs.compile(open(file, encoding='utf-8').read(), cwd='C:\\Users\\xiongda\\AppData\\Roaming\\npm\\node_modules')


def get_response_body(response):
    return ctx.call('first_decrypt', response)


if __name__ == '__main__':
    print('haha')
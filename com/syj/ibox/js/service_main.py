import execjs


file = 'services.js'

with open(file, encoding='utf-8') as f:
    content = f.read()
    if '\xa0' in content:
        begin = content.find('\xa0')
        target = content[begin: begin + 1000]
        print(target)

ctx = execjs.compile(open(file, encoding='utf-8').read(), cwd=r'C:\Users\xiongda\AppData\Roaming\npm\node_modules')


params = {}
params['path'] = "/nft-mall-web/v1.2/nft/product/getResellList?type=0&origin=0&sort=0&page=1&pageSize=50"
params['timestamp'] = 1657709076191
params['key'] = 'vyWNDaimVvUcm+18hqopqA=='
params['token'] = '58_7U5LowsMIYiqOuoL4IhAHHQ4Z9vdbBkRkgh5DWUdsIPMmfPm-VWKg2HgV71IQOapzcps5FWF-W5kQf7I'
params['vip'] = '109.244.145.199'

js = f'get_container_data({params})'
print(js)
result = ctx.eval(js)
print(result)
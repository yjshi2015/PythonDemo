from aiohttp import ClientPayloadError
from loguru import logger
import aiohttp
import asyncio
import base64
import json

base_url = 'https://api.hunliji.com/hms/eInvitation/appApi/card/v2/preview?cardId='
home_url = 'https://www.hunliji.com/p/frontend/creation-platform/app-preview-wedding-card/dist/index.html?cardId='

semaphore = asyncio.Semaphore(5)
error_num = 0


async def scraw(card_id_base64):
    try:
        async with semaphore:
            async with aiohttp.ClientSession() as session:
                async with session.get(base_url + card_id_base64) as response:
                    return await response.text()
    except ClientPayloadError as e:
        logger.error('scraw card_id_base64 {} occur error', card_id_base64, e)


async def get_data():
    # cailichao_id = 68809123
    tasks = []
    # 60400001即2022/01/01
    card_id , target = 60400001, 60500002
    # card_id , target = 60400001, 60400002
    while card_id < target:
        suffix = 'fire_cloud'
        card_id_str = str(card_id) + suffix
        card_id_base64 = base64.b64encode(card_id_str.encode()).decode()
        # logger.info('card_id: {}, card_id_base64: {}', card_id_str, card_id_base64)

        task = asyncio.ensure_future(scraw(card_id_base64))
        tasks.append(task)
        card_id += 1
        if len(tasks) % 5000 == 0:
            logger.info('来一波')
            results = await asyncio.gather(*tasks)
            save_data(results)
            tasks = []
    if len(tasks) > 0:
        logger.info('清理库存')
        results = await asyncio.gather(*tasks)
        save_data(results)


def save_data(results):
    global error_num
    for response_content in results:
        try:
            json_content = json.loads(response_content)
            status_info = json_content['status']
            if status_info['retCode'] != 0:
                # logger.error('response status error: {}', status_info)
                error_num += 1
                continue
            data_info = json_content['data']
            page_list = data_info['pages']
            user_base = data_info['userBase']
            wedding_pics = []
            for page in page_list:
                page_content = page['pageContent']
                elements = json.loads(page_content)['elements']
                for element in elements:
                    if element['type'] == 'image':
                        clipurl = element['element']['view']['clipURL']
                        wedding_pics.append(clipurl)
            wedding_info = {
                'cardId': data_info['cardId'],
                'cardIdEncrypt': data_info['cardIdEncrypt'],
                'userId': data_info['userId'],
                'groomName': user_base.get('groomName'),
                'brideName': user_base.get('brideName'),
                'time': user_base.get('time'),
                'place': user_base.get('place'),
                'longtitude': user_base.get('longtitude'),
                'latitude': user_base.get('latitude'),
                'home_url': home_url + data_info['cardIdEncrypt'],
                'weding_pics': ';'.join(wedding_pics),
                'all_content': data_info
            }
            if wedding_info['brideName'] and '刘聪' in wedding_info['brideName']:
                print(wedding_info)
        except Exception as e:
            logger.error('parse result error, card_id:{}', json.loads(response_content).get('data').get('cardId'))
            logger.exception(e)
    logger.info('共有{}条记录不存在', error_num)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(get_data())

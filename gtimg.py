# -*- coding: UTF-8 -*-
# Tencent stock data

import requests
import time
from tornado.httpclient import AsyncHTTPClient
from .base import log
from .sina import prefix

logger = log.Log()

base_url = 'http://data.gtimg.cn/flashdata/hushen/daily/'

# Synchronization methods
def daily_year(code, year='19'):
    url = base_url + year + '/' + prefix(code) + '.js?visitDstTime=1'
    response = requests.get(url)
    if response.status_code != 200:
        logger.error('Request error with stock code :' + code + ' ,response code: ' + response.status_code)
    alt = parse(response.text)
    return alt

async def daily_year_async(code, year='19'):
    url = base_url + year + '/' + prefix(code) + '.js?visitDstTime=1'
    response = await AsyncHTTPClient().fetch(url)
    if response.code != 200:
        logger.error('Request error with stock code :' + code + ' ,response code: ' + response.code)
    html = response.body if isinstance(response.body, str) else response.body.decode()
    alt = parse(html)
    return alt

def parse(str):
    lt = str.split('\n')[1:-1]
    alt = []
    for item in lt:
        tmp = item.split(' ')
        tmp[5] = int(tmp[5].replace('\\n\\', ''))
        tmp[0] = int(time.mktime(time.strptime(tmp[0], '%y%m%d')) * 1000)
        for i in range(1, 5):
            tmp[i] = float(tmp[i])
        alt.append(tmp)
    return alt




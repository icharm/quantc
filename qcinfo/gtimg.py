# -*- coding: UTF-8 -*-
# QCInfo
# Tencent Stock data
# Version 0.1

import time
from .basic import *

logger = log.Log()

base_url = 'http://data.gtimg.cn/flashdata/hushen'

# Synchronization methods
def daily_year(code, year='19'):
    '''
    Daily nodes of whole year.
    :param code: stock code
    :param year: year 19 means 2019
    :return: None or List [{'date': 1552233600000, 'open': 7.0, 'close': 7.24, 'high': 7.25, 'low': 7.0, 'volume': 698387}, ...]
    '''
    url = base_url + year + '/daily/' + prefix(code) + '.js?visitDstTime=1'
    content = request(url)
    if content is None:
        return None
    return parse(content)

async def daily_year_async(code, year='19'):
    url = base_url + year + '/daily/' + prefix(code) + '.js?visitDstTime=1'
    content = await asyncrequest(url)
    if content is None:
        return None
    return parse(content)

def daily_lately(code):
    '''
    100 daily nodes lately.
    :param code: stock code
    :return: None or List
    '''
    url = base_url + '/latest/daily/' + prefix(code) + '.js?maxage=43201&visitDstTime=1'
    content = request(url)
    if content is None:
        return None
    return parse(content, 2)

async def daily_lately_async(code):
    url = base_url + '/latest/daily/' + prefix(code) + '.js?maxage=43201&visitDstTime=1'
    content = await asyncrequest(url)
    if content is None:
        return None
    return parse(content, 2)

def weekly_lately(code):
    '''
    100 Weekly nodes lately.
    :param code: stock code
    :return: None or List
    '''
    url = base_url + '/latest/weekly/' + prefix(code) + '.js?maxage=43201&visitDstTime=1'
    content = request(url)
    if content is None:
        return None
    return parse(content, 2)

async def weekly_lately_async(code):
    url = base_url + '/latest/weekly/' + prefix(code) + '.js?maxage=43201&visitDstTime=1'
    content = await asyncrequest(url)
    if content is None:
        return None
    return parse(content, 2)

def weekly(code):
    url = base_url + '/weekly/' + prefix(code) + '.js?maxage=43201&visitDstTime=1'
    content = request(url)
    if content is None:
        return None
    return parse(content, 2)

async def weekly_async(code, retformat='dict', timeformat='str'):
    url = base_url + '/weekly/' + prefix(code) + '.js?maxage=43201&visitDstTime=1'
    content = await asyncrequest(url)
    if content is None:
        return None
    return parse(content, 2, retformat, timeformat)

def parse(str, flag=1, retformat='dict', timeformat='str'):
    lt = str.split('\n')[flag:-1]
    alt = []
    for item in lt:
        tmp = item.split(' ')
        tmp[5] = int(tmp[5].replace('\\n\\', ''))
        if timeformat == 'str':
            tmp[0] = time.strftime('%Y-%m-%d', time.strptime(tmp[0], '%y%m%d'))
        elif timeformat == 'int':
            tmp[0] = int(time.mktime(time.strptime(tmp[0], '%y%m%d')) * 1000)
        for i in range(1, 5):
            tmp[i] = float(tmp[i])
        if retformat == 'dict':
            alt.append({
                'date': tmp[0],
                'open': tmp[1],
                'close': tmp[2],
                'high': tmp[3],
                'low': tmp[4],
                'volume': tmp[5]
            })
        elif retformat == 'list':
            alt.append(tmp)
        else:
            alt = None
    return alt


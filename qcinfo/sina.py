# -*- coding: UTF-8 -*-
# Sina stock data
import re
from .basic import *

logger = log.Log()

base_url = 'http://hq.sinajs.cn/list='

def quotes(code):
    url = base_url + prefix(code)
    response = request(url)
    if response is None:
        return None
    return parse(response)

async def quotes_async(code):
    url = base_url + prefix(code)
    content = await asyncrequest(url, encode='gbk')
    if content is None:
        return None
    return parse(content)

def quotes_multiple(codes):
    all = ''
    for code in codes:
        all += prefix(code) + ','
    all = all[:-1]
    url = base_url + all
    response = request(url)
    if response is None:
        return None
    return parse_multiple(response)

async def quotes_multiple_async(codes):
    all = ''
    for code in codes:
        all += prefix(code) + ','
    all = all[:-1]
    url = base_url + all
    content = await asyncrequest(url, encode='gbk')
    if content is None:
        return None
    return parse_multiple(content)

def parse(strs):
    # strs = 'var hq_str_sh601003="柳钢股份,7.240,7.280,7.280,7.360,7.220,7.270,7.280,14663112,106848071.000,100348,7.270,221500,7.260,147100,7.250,158000,7.240,296500,7.230,174200,7.280,164700,7.290,189801,7.300,44200,7.310,99900,7.320,2019-02-20,15:00:00,00";'
    if len(strs) < 25:
        logger.error('No quotes data. ' + strs)
        return None
    lt = strs.split(',')
    result = re.match(r'(.*)([0-9]{6})="(.*)', lt[0])
    return {
        'code': result[2],
        'name': result[3],
        'open': float(lt[1]),
        'now': float(lt[3]),
        'close': float(lt[2]), # 昨日收盘价
        'high': float(lt[4]),
        'low': float(lt[5]),
        'money': round(float(lt[9]), 3),
        'volume': int(lt[8]),
        'date': lt[30]
    }

def parse_multiple(strs):
    lt = strs.split(';\n')
    data = {}
    for item in lt:
        if item == '':
            continue
        dt = parse(item)
        if dt is not None:
            data[dt['code']] = dt
    return data
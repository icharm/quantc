# -*- coding: UTF-8 -*-
# Sina stock data
import requests
import re
from tornado.httpclient import AsyncHTTPClient
from basic import log

logger = log.Log()

base_url = 'http://hq.sinajs.cn/list='

def prefix(code):
    # '00': // 深交所A股
    # '20': // 深交所B股
    # '30': // 深交所创业板
    # '60': // 上交所A股
    # '90': // 上交所B股
    two = code[0:2]
    if two == '00' or two == '20' or two == '30':
        code = 'sz' + code
    else:
        code = 'sh' + code
    return code

def quotes(code):
    url = base_url + prefix(code)
    response = requests.get(url)
    data_str = response.text
    return parse(data_str)

async def quotes_async(code):
    url = base_url + prefix(code)
    response = await AsyncHTTPClient().fetch(url)
    if response.code != 200:
        logger.error('Request error with stock code :' + code + ' ,response code: ' + response.code)
    content = response.body if isinstance(response.body, str) else response.body.decode('gbk')
    return parse(content)

def quotes_multiple(codes):
    all = ''
    for code in codes:
        all += prefix(code) + ','
    all = all[:-1]
    url = base_url + all
    response = requests.get(url)
    data_str = response.text
    return parse_multiple(data_str)

async def quotes_multiple_async(codes):
    all = ''
    for code in codes:
        all += prefix(code) + ','
    all = all[:-1]
    url = base_url + all
    response = await AsyncHTTPClient().fetch(url)
    if response.code != 200:
        logger.error('Request error with stock code :' + code + ' ,response code: ' + response.code)
    content = response.body if isinstance(response.body, str) else response.body.decode('gbk')
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
        'close': float(lt[3]),
        'high': float(lt[4]),
        'low': float(lt[5]),
        'money': lt[9],
        'volume': float(lt[8]),
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
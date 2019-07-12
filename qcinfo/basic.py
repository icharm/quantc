# -*- coding: UTF-8 -*-
# Basic method for qcinfo.
import requests
from tornado.httpclient import AsyncHTTPClient
from basic import log

logger = log.Log()

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

def request(url, headers=[]):
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        logger.error('Request error url:' + url + ' ,response code: ' + str(response.status_code))
        return None
    return response.text

async def asyncrequest(url, encode='utf-8', header={}):
    response = await AsyncHTTPClient().fetch(url, headers=header, validate_cert=False)
    if response.code != 200:
        logger.error('Request error url:' + url + ' ,response code: ' + str(response.code))
        return None
    html = response.body if isinstance(response.body, str) else response.body.decode(encode)
    return html
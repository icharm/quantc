# -*- coding: UTF-8 -*-
import requests
import json
from ..base import log

logger = log.Log()

# Request headers
headers = {
    'Host': 'webapi.cninfo.com.cn',
    'Content-Length': '0',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Accept': '*/*',
    'Origin': 'http://webapi.cninfo.com.cn',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
    'Referer': 'http://webapi.cninfo.com.cn/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': '',
    'Connection': 'close'
}

# Base webapi url
webapi = 'http://webapi.cninfo.com.cn'
# Cninfo url
cninfo_url = 'http://www.cninfo.com.cn'

def categorys(type = None):
    '''
    :param type:    None default all category
                    'S' 申万行业分类
                    '0' 证监会行业分类
                    'Z' 国证行业分类
                    'T' 地区分类
                    'Y' 指数分类
                    '1' 市场分类
    :return:    dict or None
    '''
    url = webapi + '/api/sysapi/p_sysapi1016'
    response = requests.post(url, headers=headers)
    dt = json.loads(response.text)
    if dt.get('resultcode', '') != 200:
        logger.error('Request failed, ' + str(dt))
        return None
    logger.info('Requested sucessfully.')
    if type == None:
        return dt.get('records')
    if type == 'S':
        return dt.get('records')[0]
    if type == '0':
        return dt.get('records')[1]
    if type == 'Z':
        return dt.get('records')[2]
    if type == 'T':
        return dt.get('records')[3]
    if type == 'Y':
        return dt.get('records')[4]
    if type == '1':
        return dt.get('records')[5]

# stocks
def stocks_under_category(param, url='/api/stock/p_public0004'):
    '''
    record:{
      'F009V': 'S11',
      'F007V': '饲料',
      'F008V': None,
      'F006V': '饲料',
      'F005V': '饲料',
      'SECNAME': '*ST康达',
      'STARTDATE': '2011-10-10 00:00:00',
      'F013V': None,
      'SECCODE': '000048',
      'F004V': '农林牧渔',
      'F010V': 'S1104',
      'F012V': None,
      'F003V': 'S110401',
      'F001V': '137004',
      'F002V': '申银万国行业分类',
      'F011V': 'S110401'
      }
    '''
    url = webapi + url + '?' + param
    response = requests.get(url, headers=headers)
    dt = json.loads(response.text)
    # print(response.text)
    if dt.get('resultcode') != 200:
        logger.error('Request failed. ' + str(dt))
    return dt.get('records')

# Daily line data
def daily_line(scode, is_parse=True):
    '''
    line_node:{
        0:"TIME",
        1:"OPEN",
        2:"CLOSE",
        3:"HIGH",
        4:"LOW",
        5:"MONEY",
        6:"VOL",
        7:"KZHANGDIEFU",
        8:"KZHANGDIE"
    }
    :param scode: SECCODE
    :return: list line_node or None
    '''
    url = cninfo_url + '/data/cube/dailyLine?stockCode=' + scode
    response = requests.get(url)
    if response.status_code != 200:
        logger.error('Request failed, ' + str(response))
    if not is_parse:
        return response.text
    dt = json.loads(response.text)
    return dt['line']
# -*- coding: UTF-8 -*-
# Stock data fetch from website.
from basic import log
from . import xueqiu as XQ
from . import gtimg

logger = log.Log()

async def company_info_async(code):
    '''
    上市公司基本信息
    :param code: Stock code
    :return:
    '''
    return await XQ.company_info_async(code)

def quotes_lately(code, type="d"):
    '''
    最近的100条行情数据列表
    :param code: Stock code
    :param type: d：daily, w: weekly
    :return: list
    '''
    if type == "d":
        return gtimg.daily_lately(code)
    else:
        return gtimg.weekly_lately(code)
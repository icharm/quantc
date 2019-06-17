# -*- coding: UTF-8 -*-
# Stock data fetch from website.
from qcinfo import xueqiu as XQ
from qcinfo import qcrepo, gtimg
from qcinfo.log import qcinfo_log

logger = qcinfo_log()

async def company_info_async(code):
    '''
    上市公司基本信息
    :param code: Stock code
    :return:
    '''
    return await XQ.company_info_async(code)

def quotes(code, type="d"):
    '''
    所有行情数据列表
    :param code: Stock code
    :param type: d：daily, w: weekly
    :return: dateframe
    '''
    return qcrepo.quotes(code, type)

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

def is_trading(date):
    '''
    是否为交易日
    :param date: %Y-%d-%m
    :return: True : yes, False: no
    '''
    cal = qcrepo.calendar()
    df = cal.loc[cal['date'] == date]
    if df.iloc[0]["open"] == 1:
        return True
    else:
        return False
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

############################## Calendar ####################################

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

def calendar():
    '''
    交易日历
    :return: pandas.DataFrame(data=content, columns=["date", "open", "weekday"]) 日期 是否交易日 星期
    '''
    return qcrepo.calendar()

def last_trading_day_week(date):
    '''
    本周中最后一个交易日
    :param date: String %Y-%m-%d
    :return: date string or none(no trading day this week)
    '''
    cdf = calendar()
    last = None
    for index, row in cdf.iterrows():
        if row["date"] == date:
            week_start_index = index - row["weekday"]
            for index1, row1 in cdf.iloc[week_start_index:week_start_index+7].iterrows():
                if row1["open"] == 1:
                    last = row1["date"]
    return last

def islast_trading_day_week(date):
    '''
    是否为本周最后一个交易日
    :param date: String %Y-%m-%d
    :return: true or false
    '''
    if last_trading_day_week(date) == date:
        return True
    else:
        return False
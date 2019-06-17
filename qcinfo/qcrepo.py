# -*- coding: UTF-8 -*-
import os
from qcinfo.log import qcinfo_log
import traceback
import pandas
from os.path import dirname
import json

logger = qcinfo_log()

DK="k/d/%s.json"
WK="k/w/%s.json"
MK="k/m/%s.json"
M10K="k/m10/%s.json"
STOCKS="stocks.json"
CALENDAR="calendar.json"

dir = dirname(__file__)+ '/store/'

def quotes(code, type="d"):
    '''
    行情列表
    :param code:
    :param type:
    :return: DataFrame(Series(["time", "open", "close", "high", "low", "amount", "volume", "percent", "change", "turnover_rate"]))
        时间戳，开盘价，收盘价，最高价，最低价，成交金额，成交量，涨跌幅%，涨跌金额，换手率
    '''
    try:
        if type == "d":
            file = ropen(dir + DK % (code))
            content = file.read()
            df = pandas.DataFrame(data=json.loads(content), columns=["time", "open", "close", "high", "low", "amount", "volume", "percent", "change", "turnover_rate"])
            file.close()
        else:
            df = None
        return df
    except:
        logger.error(traceback.format_exc())
        return None

def stocks():
    '''
    股票列表
    :return: DataFrame(columns=["seccode", "secname", "sdate", "mtype", "ptype"]) 代码 名称 上市日期 交易所 板块
    '''
    file = ropen(dir + STOCKS)
    content = file.read()
    file.close()
    content = json.loads(content)
    return pandas.DataFrame(data=content)

def calendar():
    '''
    交易日历
    :return: pandas.DataFrame(data=content, columns=["date", "open", "weekday"]) 日期 是否交易日 星期
    '''
    try:
        file = ropen(dir + CALENDAR)
        content = json.loads(file.read())
        file.close()
        df = pandas.DataFrame(data=content, columns=["date", "open", "weekday"])
        return df
    except:
        logger.error(traceback.format_exc())

def set_stocks(content):
    try:
        file = open(dir + STOCKS, mode="w", encoding='utf8')
        file.write(content)
        file.close()
    except:
        logger.error(traceback.format_exc())

def set_quotes(code, type="d", content=""):
    try:
        if type == "d":
            file = wopen(dir + DK % (code))
            file.write(content)
            file.close()

    except:
        logger.error(traceback.format_exc())

def append_quotes(code, type="d", content=""):
    '''
    追加行情数据
    :param code:
    :param type:
    :param content: json str
    :return:
    '''
    try:
        if type == "d":
            file = wopen(dir + DK % (code), mode="a")
            file.seek(file.tell() - 1, os.SEEK_SET) # pointer to last char
            file.truncate() # delete last char
            file.write(","+content+"]")
            file.close()
        return True
    except:
        logger.error(traceback.format_exc())
        return False

def ropen(file):
    return open(file, mode="r", encoding='utf8')

def wopen(file, mode="a"):
    return open(file, mode=mode, encoding='utf8')
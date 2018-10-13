# -*- coding: UTF-8 -*- 
import http.client
import urllib
import json
import log
import base

log = log.Log('tradeDate.py')

class TradeDate:
    date = ''                #F001D  日期	        date
    isFirstDayOfWeek = ''    #F002C  是否周初	    varchar	0-否；1-是；默认为0
    isLastDayOfWeek = ''     #F003C  是否周末	    varchar	0-否；1-是；默认为0
    isFirstDayOfMonth = ''	 #F004C  是否月初	    varchar	0-否；1-是；默认为0
    isLastDayOfMonth = ''    #F005C	是否月末	    varchar	0-否；1-是；默认为0
    isTradingDay = ''        #F006C	是否交易日	    varchar	0-否；1-是；默认为0
    isLastDayOfSeason = ''   #F007C	是否季末	    varchar	0-否；1-是；默认为0
    isLastDayOfHalfYear = '' #F008C	是否半年末	    varchar	0-否；1-是；默认为0
    isLastDayOfYear = ''     #F009C  是否年末	    varchar	0-否；1-是；默认为0
    isBankTradingDay = ''    #F010C	是否银行间交易日 varchar 0-否；1-是；默认为0
    previousTradingDay = ''  #F011D  前一交易日	    date	
    nextTradingDay = ''      #F012D  后一交易日	    date

def parse(dict):
    """
    Parse dict to TradeDate object.

    Args: dict
    Returns: TradeDate object
    """
    obj = TradeDate()
    obj.date = dict['F001D']
    obj.isFirstDayOfWeek = dict['F002C']
    obj.isLastDayOfWeek = dict['F003C']
    obj.isFirstDayOfMonth = dict['F004C']
    obj.isLastDayOfMonth = dict['F005C']
    obj.isTradingDay = dict['F006C']
    obj.isLastDayOfSeason = dict['F007C']
    obj.isLastDayOfHalfYear = dict['F008C']
    obj.isLastDayOfYear = dict['F009C']
    obj.isBankTradingDay = dict['F010C']
    obj.previousTradingDay = dict['F011D']
    obj.nextTradingDay = dict['F012D']
    return obj

def callService(sdate, edate, status):
    """
    Query cninfo trading date api by call base.py callService method.

    Args:
        sdate: start date, support format：20161101 or 2016-11-01 or 2016/11/01
        edate: end date
        status: trading status,  1: trading day  2: closed day , multiple inputs is not supported.
    
    Returns:
        1. None： not data.
        2. TradeDate Object.
        3. Dict: {date:TradeDateObject, ...}
    """
    url = 'http://webapi.cninfo.com.cn/api/stock/p_public0001'
    params = {
        'sdate': sdate,
        'edate': edate,
    }
    if status != '':
        params['state'] = status
    respContent = base.callService(url, params)
    if respContent == None:
        return None
    dataDict = respContent['records']
    count = respContent['count']
    if count == 0:
        log.info('No data form serivce')
        return None
    elif count == 1:
        return parse(dataDict[0])
    else:
        dict = {}
        for item in dataDict:
            obj = parse(item)
            dict[obj.date] = obj
        return dict

def certainDate(date):
    ''' Get date info of certain date '''
    return callService(date, date, '')

def dateRange(sdate, edate):
    ''' Get date info dict of certain date range
    Args:
        sdate: start date.
        edate: end date.
    Returns:
        TradeDate object dict, eg: {date:TradeDateObject, ..., ...}
    '''
    return callService(sdate, edate, '')

def tradingDayOfRange(sdate, edate):
    ''' Get trading day dict of certain date range
    Args:
        sdate: start date.
        edate: end date.
    Returns:
        TradeDate object dict, eg: {date:TradeDateObject, ..., ...}
    '''
    return callService(sdate, edate, 1)

def closedDayOfRange(sdate, edate):
    ''' Get trading day dict of certain date range
    Args:
        sdate: start date.
        edate: end date.
    Returns:
        TradeDate object dict, eg: {date:TradeDateObject, ..., ...}
    '''
    return callService(sdate, edate, 0)


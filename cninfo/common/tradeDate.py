# -*- coding: UTF-8 -*- 
import http.client
import urllib
import json
from base import log
from base import base

log = log.Log(__name__)

class TradeDate:
    date = ''                   #F001D  日期	        date
    is_first_day_week = ''      #F002C  是否周初	    varchar	0-否；1-是；默认为0
    is_last_day_week = ''       #F003C  是否周末	    varchar	0-否；1-是；默认为0
    is_first_day_month = ''	    #F004C  是否月初	    varchar	0-否；1-是；默认为0
    is_last_day_month = ''      #F005C	是否月末	    varchar	0-否；1-是；默认为0
    is_trading_day = ''         #F006C	是否交易日	    varchar	0-否；1-是；默认为0
    is_last_day_season = ''     #F007C	是否季末	    varchar	0-否；1-是；默认为0
    is_last_day_halfyear = ''   #F008C	是否半年末	    varchar	0-否；1-是；默认为0
    is_last_day_year = ''       #F009C  是否年末	    varchar	0-否；1-是；默认为0
    is_bank_trading_day = ''    #F010C	是否银行间交易日 varchar 0-否；1-是；默认为0
    previous_trading_day = ''   #F011D  前一交易日	    date	
    next_trading_day = ''       #F012D  后一交易日	    date

    def __init__(self, dict):
        self.parse(dict)

    def parse(self, dict):
        """
        Parse dict to TradeDate object.

        Args: dict
        Returns: TradeDate object
        """
        self.date = dict['F001D']
        self.is_first_day_week = dict['F002C']
        self.is_last_day_week = dict['F003C']
        self.is_first_day_month = dict['F004C']
        self.is_last_day_month = dict['F005C']
        self.is_trading_day = dict['F006C']
        self.is_last_day_season = dict['F007C']
        self.is_last_day_halfyear = dict['F008C']
        self.is_last_day_year = dict['F009C']
        self.is_bank_trading_day = dict['F010C']
        self.previous_trading_day = dict['F011D']
        self.next_trading_day = dict['F012D']

def call(sdate, edate, status):
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
    url = '/api/stock/p_public0001'
    params = {
        'sdate': sdate,
        'edate': edate,
    }
    if status != '':
        params['state'] = status
    resp = base.call(url, params)
    if resp == '':
        return ''
    resp = json.loads(resp)
    records = resp['records']
    count = resp['count']
    if count == 0:
        log.info('No data form serivce')
        return ''
    elif count == 1:
        return TradeDate(records[0])
    else:
        trade_dates = {}
        for item in records:
            obj = TradeDate(item)
            trade_dates[obj.date] = obj
        return trade_dates

def certain(date):
    ''' Get date info of certain date

    Args:
        date: certain date.
    Returns:
        TradeDate object.
    '''
    return call(date, date, '')

def range(sdate, edate):
    ''' Get date info dict of certain date range

    Args:
        sdate: start date.
        edate: end date.
    Returns:
        TradeDate object dict, eg: {date:TradeDateObject, ..., ...}
    '''
    return call(sdate, edate, '')

def trading_range(sdate, edate):
    ''' Get trading day dict of certain date range

    Args:
        sdate: start date.
        edate: end date.
    Returns:
        TradeDate object dict, eg: {date:TradeDateObject, ..., ...}
    '''
    return call(sdate, edate, 1)

def closed_range(sdate, edate):
    ''' Get trading day dict of certain date range

    Args:
        sdate: start date.
        edate: end date.
    Returns:
        TradeDate object dict, eg: {date:TradeDateObject, ..., ...}
    '''
    return call(sdate, edate, 0)


# -*- coding: UTF-8 -*- 
import http.client
import urllib
import json
from cninfo import D
from base import log
from base import base

log = log.Log(__name__)

def call(sdate, edate, status):
    """
    Query cninfo trading date api by call base.py callService method.

    Args:
        sdate: start date, support format：20161101 or 2016-11-01 or 2016/11/01
        edate: end date
        status: trading status,  1: trading day  2: closed day , multiple inputs is not supported.
    
    Returns:
        1. None： not data.
        2. One record, day dict.
        3. List: [day1_dict, day2_dict, ....]
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
    return D.Day.parses(records, count)

def certain(date):
    ''' Get date info of certain date

    Args:
        date: certain date.
    Returns:
        Day dict.
        See the D.Day annotation for field details.
    '''
    return call(date, date, '')

def range(sdate, edate):
    ''' Get date info dict of certain date range

    Args:
        sdate: start date.
        edate: end date.
    Returns:
        List: [day1_dict, day2_dict, ....]
        See the D.Day annotation for field details.
    '''
    return call(sdate, edate, '')

def trading_range(sdate, edate):
    ''' Get trading day dict of certain date range

    Args:
        sdate: start date.
        edate: end date.
    Returns:
        List: [day1_dict, day2_dict, ....]
        See the D.Day annotation for field details.
    '''
    return call(sdate, edate, 1)

def closed_range(sdate, edate):
    ''' Get trading day dict of certain date range

    Args:
        sdate: start date.
        edate: end date.
    Returns:
        List: [day1_dict, day2_dict, ....]
        See the D.Day annotation for field details.
    '''
    return call(sdate, edate, 0)


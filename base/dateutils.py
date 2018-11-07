# -*- coding: UTF-8 -*- 
import time

from . import log

logger = log.Log(__name__)

DF_FULL_NORMAL = '%Y-%m-%d'
DTF_FULL_NORMAL = '%Y-%m-%d %X'

def current(format):
    ''' Get current date, no time
    Agrs: 
        format: date format, for example: '%Y-%m-%d' or '%Y%m%d' or '%Y/%m/%d' ...
    Returns:
        string date according to format.
    '''
    return time.strftime(format, time.localtime())

def seconds(datetime, format):
    ''' String datetime to total seconds.
    '''
    try:
        st = time.strptime(datetime, format)
        return time.mktime(st)
    except Exception as e:
        logger.error(str(e))
        return 0

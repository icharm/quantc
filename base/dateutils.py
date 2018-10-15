# -*- coding: UTF-8 -*- 
import time

DF_FULL_NORMAL = '%Y-%m-%d'
DTF_FULL_NORMAL = '%Y-%m-%d %X'

def currentDate(format):
    ''' Get current date, no time
    Agrs: 
        format: date format, for example: '%Y-%m-%d' or '%Y%m%d' or '%Y/%m/%d' ...
    Returns:
        string date according to format.
    '''
    return time.strftime(format, time.localtime())
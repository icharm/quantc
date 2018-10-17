# -*- coding: UTF-8 -*- 
from base import config
from base import log

log = log.Log(__name__)

def set(fileName, content):
    try:
        file = open(config.cache_root_path + fileName, 'w+', encoding='utf8')
        file.write(content)
        file.close()
    except Exception as e:
        log.error(str(e))

def get(fileName):
    try:
        file = open(config.cache_root_path + fileName, 'r', encoding='utf8')
        content = file.read()
        file.close()
        return content
    except Exception as e:
        log.error(str(e))
        return ''

def spliceFileName(fileName, params):
    '''According params dict to splice full cache file name.
    Args:
        fileName: str, cache file name prefix.
        params: dict, request params or other dict.
    Return:
        string, full file name
    '''
    values = params.values()
    for value in values:
        if value != '':
            fileName = fileName + '_' + value
    return fileName

def setWithParams(fileName, params, content):
    '''According params dict to cache content.
    Args:
        fileName: str, cache file name prefix.
        params: dict, request params or other dict.
        content: str, cache content.
    '''
    return set(spliceFileName(fileName, params), content)

def getWithParams(fileName, params):
    '''According params dict to get cache content.
    Args:
        fileName: str, cache file name prefix.
        params: dict, request params or other dict.
    Returns:
        str, cache content.
        if can't find cache file, then return ''
    '''
    return get(spliceFileName(fileName, params))

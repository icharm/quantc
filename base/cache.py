# -*- coding: UTF-8 -*- 
from base import config
from base import log

log = log.Log(__name__)

def set(filename, content):
    try:
        file = open(config.cache_root_path + filename, 'w+', encoding='utf8')
        file.write(content)
        file.close()
    except Exception as e:
        log.error(str(e))

def get(filename):
    try:
        file = open(config.cache_root_path + filename, 'r', encoding='utf8')
        content = file.read()
        file.close()
        return content
    except Exception as e:
        log.error(str(e))
        return ''

def splice_filename(filename, params):
    '''According params dict to splice full cache file name.
    Args:
        filename: str, cache file name prefix.
        params: dict, request params or other dict.
    Return:
        string, full file name
    '''
    items = params.items()
    for key,value in items:
        if key == 'access_token':
            continue
        if value != '':
            filename = filename + '_' + value
    return filename

def set_params(filename, params, content):
    '''According params dict to cache content.
    Args:
        filename: str, cache file name prefix.
        params: dict, request params or other dict.
        content: str, cache content.
    '''
    if isinstance(content, bytes):
        content = str(content, encoding='utf8')
    return set(splice_filename(filename, params), content)

def get_params(filename, params):
    '''According params dict to get cache content.
    Args:
        filename: str, cache file name prefix.
        params: dict, request params or other dict.
    Returns:
        str, cache content.
        if can't find cache file, then return ''
    '''
    return get(splice_filename(filename, params))

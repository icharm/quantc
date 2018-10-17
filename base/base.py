# -*- coding: UTF-8 -*- 
import http.client
import urllib
import json

from base import config
from base import log
from base import cache

log = log.Log(__name__)

def getAccessToken():
    '''Main entrance to get access_token, first, get token from cache file
    if token is '', then update it from service.
    '''
    token = cache.get(config.token)
    if token.strip() == '':
        token = getAccessTokenFromService()
    return token

def getAccessTokenFromService():
    '''Get access_token form service and update it into cache.
    '''
    url = 'http://webapi.cninfo.com.cn/api-cloud-platform/oauth2/token'
    params = {
        'grant_type' : 'client_credentials',
        'client_id' : config.access_key,
        'client_secret' : config.access_sercet
    }
    paramsbyte = bytes(urllib.parse.urlencode(params), 'utf8')
    response = urllib.request.urlopen(url, paramsbyte)
    respContent = response.read()
    dataDict=json.loads(respContent)
    token=dataDict['access_token']
    cache.set(config.token, token)
    return token

def callService(url, params):
    '''Main function to call cninfo services.
    Args:
        url: api url. String
        params: request params. Dict
    Returns:
        if service return code is not 200, then return None.
        if call service success, then return response dict.
    '''
    params['access_token'] = getAccessToken()
    paramsbyte = bytes(urllib.parse.urlencode(params), 'utf8')
    response = urllib.request.urlopen(config.base_url+url, paramsbyte)
    respContent = response.read()
    respContent = json.loads(respContent)
    respCode = respContent['resultcode']
    if respCode == 401 or respCode == 404 or respCode == 405:
        log.debug('Token invalid. Updating it form service')
        getAccessTokenFromService()
        return callService(url, params)
    elif respCode != 200:
        log.error('Api调用出错：' + respContent['resultmsg'])
        return None
    else:
        return respContent
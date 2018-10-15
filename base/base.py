# -*- coding: UTF-8 -*- 
import http.client
import urllib
import json

from base import config
from base import log

log = log.Log(__name__)

# Main entrance to get token
def getAccessToken():
    token = getAccessTokenFromCache()
    if token.strip() == '':
        token = getAccessTokenFromService()
    return token

# Cache token into file
def cacheAccessToken(token):
    path = config.token_path
    file = open(path, 'w+')
    file.write(token)
    file.close()

# Get token from cache file
def getAccessTokenFromCache():
    path = config.token_path
    file = open(path, 'r')
    token = file.read()
    file.close()
    return token

# Get token from cninfo service
def getAccessTokenFromService():
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
    cacheAccessToken(token)
    return token

# Main function to call cninfo service
def callService(url, params):
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
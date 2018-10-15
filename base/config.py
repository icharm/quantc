# -*- coding: UTF-8 -*- 
from os.path import dirname
# 巨潮资讯数据API
access_key = '626b1fe5c1df4a878c91949aafba7f59'
access_sercet = '4127670dfbfa4fa791b4a5c4bb6bad69'
base_url = 'http://webapi.cninfo.com.cn'

# Access token cache file path
token_path = dirname(dirname(__file__))+'\\cache\\token'
# Log file path
log_path = dirname(dirname(__file__))+'\\log\\log'
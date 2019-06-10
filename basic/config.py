# -*- coding: UTF-8 -*- 
from os.path import dirname

# --------- #
#   API     #
# --------- #
access_key = '626b1fe5c1df4a878c91949aafba7f59'
access_sercet = '4127670dfbfa4fa791b4a5c4bb6bad69'
base_url = 'http://webapi.cninfo.com.cn'

# --------- #
#   Cache   #
# --------- #
# Cache file root path.
cache_root_path = dirname(dirname(__file__)) + '\\cache\\'
# Cache switch , if True, cacheService function (in basic.py) will read cache before call api service.
enable_cache = True
# Access token cache file name
token = 'token'
# Industry classification cache file name
cache_industry = 'industry_class'
# Region classification cache file name
cache_region = 'region_class'
# Securities category cache file name
cache_securities = 'securities_category'
# Industry classification stock list
cache_stocks_class = 'stocks_class'
# Balance sheet
cache_balance = 'balance_sheet'
# Profit sheet.
cache_profit = 'profit_sheet'

# --------- #
#   Log     #
# --------- #
# Log file path
log_path = dirname(dirname(__file__))+'/log/log'
# Console print log switch, if log_out is True, log class will print log into console and log file both.
log_out = True

# --------- #
# Database  #
# --------- #
# Db file path
db_default = dirname(dirname(__file__))+'/quantc.db'



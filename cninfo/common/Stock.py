# -*- coding: UTF-8 -*- 
import json
from base import log
from base import base

class Stock:
    code = ''           # SECCODE	证券代码	varchar
    name = ''           # SECNAME	证券简称	varchar	
    org_name = ''       # ORGNAME	机构名称	varchar	
                        # F001V	拼音简称	varchar	
    type_code = ''      # F002V	证券类别编码	varchar	
    type = ''           # F003V	证券类别	varchar	
    market_code = ''    # F004V	交易市场编码	varchar	
    market = ''         # F005V	交易市场	varchar	
    start_date = ''     # F006D	上市日期	datetime	
    start_count = ''	# F007N 初始上市数量	decimal	单位：股
    attribute_code = '' # F008V	代码属性编码	varchar	
    attribute = ''      # F009V	代码属性	varchar	
    status_code = ''    # F010V	上市状态编码	varchar	
    status = ''         # F011V	上市状态	varchar	
                        # F012N	面值	decimal	单位：元
                        # F013V	ISIN	varchar
    
    def parse(self, stock):
        self.code = stock['SECCODE']
        self.name = stock['SECNAME']
        self.org_name = stock['ORGNAME']
        self.type_code = stock['F002V']
        self.type = stock['F003V']
        self.market_code = stock['F004V']
        self.market = stock['F005V']
        self.start_date = stock['F006D']
        self.start_count = stock['F007N']
        self.attribute_code = stock['F008V']
        self.attribute = stock['F009V']
        self.status_code = stock['F010V']
        self.status = stock['F011V']

def call(codes):
    '''Query base info of stock by code.
    
    Args:
        code: stock codes, separated by comma(,), eg:000001,600000
    Returns:
        1. no data, return ''.
        2. one record, return stock object.
        3. mulitple records, return stock object dict, eg {code: object, ...}
    '''
    url = '/api/stock/p_stock2101'
    params = {
        'scode' : codes
    }
    resp = base.call(url, params)
    if resp == '':
        return ''
    resp = json.loads(resp)
    records = resp['records']
    count = resp['count']
    if count == 0:
        return ''
    elif count == 1:
        stock = Stock()
        return stock.parse(records[0])
    else:
        stocks = {}
        for record in records:
            stock = Stock()
            stock.parse(record)
            stocks[stock.code] = stock
        return stocks

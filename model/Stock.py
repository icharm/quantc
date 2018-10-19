# -*- coding: UTF-8 -*- 
class Stock:
    code = '' # SECCODE	证券代码	varchar
    name = '' # SECNAME	证券简称	varchar	

    def __init__(self, stock):
        self.parse(stock)
    
    def parse(self, stock):
        self.code = stock['SECCODE']
        self.name = stock['SECNAME']
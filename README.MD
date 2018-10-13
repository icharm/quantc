# cninfo-sdk
Packaging stock data api provided by [巨潮资讯(cninfo)](http://webapi.cninfo.com.cn/).
I always wanted to make something on the quantitative analysis, but I have not found any good stock data service for free use,
then I found cninfo.
The data provided by cninfo is more comprehensive, but an account can only call interface 1000 times for free. It is still not
clear the price of call once. I guess it should not very expensive. So I decided to use it.
Maybe I should make a database to cache some data to reduce call times.

## Requirement
Python version >= 3.0

## Api Catalog
Type | Name | File Name | Chinese
:----------- | :-----------: | :-----------: | -----------:
CommonInfo | Trading Date | tradeDate.py | 交易日历数据
 | Industry Classification | | 行业分类数据
 | Regional Classification | | 地区分类数据
 | Securities Category | | 证券类别编码数据
 | Public Coded | | 公共编码数据
 | Intermediate Exchange Rate of RMB | | 人民币汇率中间价

## Plan
First to code common info api.

## License
MIT

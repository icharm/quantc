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

### Common Info (cninfo\common)
Name | File Name | Chinese
:----------- | :-----------: | -----------:
Trading Date | TradeDate.py | 交易日历数据
Industry Classification | IndustryClass.py | 行业分类数据
Regional Classification | RegionClass.py | 地区分类数据
Securities Category | SecuritesCategory.py | 证券类别编码数据
Stock List Of Industry Classification | IndustryStocks.py | 行业股票列表
Public Coded | N/A | 公共编码数据
Intermediate Exchange Rate of RMB | N/A | 人民币汇率中间价

### Stock Info (cninfo\stock)


## Plan
First to code common info api. Obviously there is a lot of boring basic work to do, if you have any good idea,
<a href="mailto:icharm.me@outlook.com">send mail to me</a>

## License
MIT

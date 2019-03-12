# QuantC
Localized quantification tool with the goal of becoming a product similar to BigQuant, JoinQuant. The underlying data from [巨潮资讯(cninfo)](http://webapi.cninfo.com.cn/).<br>
The data provided by cninfo is more comprehensive, but an account can only call interface 1000 times for free. It is still not
clear the price of call once. I guess it should not very expensive. So I decided to use it and make a simple file cache function to reduce call times.<br>
Quantc many designs refer to BigQuant, simple and straightforward, now, it's still has few features, but I will continue to improve it.

## Requirement
Python 3.4+
pandas
highcharts
peewee-3.8.2
requests-2.21.0
pymysql-0.9.3
tornado 5.1.1

## Usage
Step 1: Goto [深证信数据服务平台(cninfo)](http://webapi.cninfo.com.cn/) register a account, and then get access_key and serect in 个人中心 - 我的凭证, copy them.
Step 2: Paste them into base/config.py

## Api Catalog

### Basic Info (cninfo\basic)
Name | File Name | Chinese
:----------- | :-----------: | -----------:
Corporation Info | Corporation.py | 上市公司基本信息

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

### Finance Info (cninfo\basic)
Name | File Name | Chinese
:----------- | :-----------: | -----------:
Balance Sheet Info | BalanceSheet.py | 资产负债表
Profit Sheet Info | ProfitSheet.py | 利润表

## Demo
http://stock.icharm.me

## Plan
First to code common info api. Obviously there is a lot of boring basic work to do, if you have any good idea,
<a href="mailto:icharm.me@outlook.com">send mail to me</a>

## License
MIT

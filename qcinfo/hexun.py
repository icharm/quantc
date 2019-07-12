# HeXun stock data, https://www.cnblogs.com/phpxuetang/p/4519446.html
import re
import json
import pandas
from .basic import *

logger = log.Log()

base_url = "http://quote.stock.hexun.com/stockdata/stock_quote.aspx?stocklist="


header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
}
######### 代码    名称     现价    涨跌幅    昨收      今开     最高    最低    成交量     成交额      换手率
Q_COLS = ['code', 'name', 'now', 'range', 'close', 'open', 'high', 'low', 'volume', 'amount', 'turnover_rate', 'unknown1', 'unknow2']

def quotes(code):
    '''
    code                600606
    name                  绿地控股
    now                   6.87
    range                 5.05
    close                 6.54
    open                  6.75
    high                  6.87
    low                   6.68
    volume              655122
    amount           444552098
    turnover_rate         0.54
    unknown1              2.91
    unknow2               2.47
    change                0.33
    '''
    url = base_url + code
    response = request(url, headers=header)
    if response is None:
        return None
    result = parse(response)
    if result is None:
        return None
    return result.iloc[0]   # 返回第一条

def quotes_multiple(codes_list):
    '''
             code  name    now  range  close   open   high    low     volume     amount  turnover_rate  unknown1  unknow2  change
    0  600606  绿地控股   6.87   5.05   6.54   6.75   6.87   6.68  655121.52  444552098           0.54      2.91     2.47    0.33
    1  002661  克明面业  13.72   1.93  13.46  13.47  13.88  13.46   32629.00   44793561           0.98      3.12     1.42    0.26
    2  600351  亚宝药业   6.01   1.01   5.95   5.95   6.03   5.93   30172.16   18087680           0.39      1.68     1.35    0.06
    '''
    codes = '|'.join(codes_list)
    url = base_url + codes
    response = request(url, headers=header)
    if response is None:
        return None
    return parse(response)


def parse(string):
    str_l = string.split(';')
    if len(str_l[0]) > 12:
        result = re.sub(r"\r\n", "", str_l[0])  # 去除回车换行
        result = re.match(r'(.*)(\[\[.*\]\])', result)
        result = result[2]
        result = re.sub(r"'", "\"", result)
        pd = pandas.DataFrame(data=json.loads(result), columns=Q_COLS)
        pd['change'] = pd.apply(lambda x: x.now - x.close, axis=1)
        return pd
    return None

# print(quotes('600606|002661|600351'))
# print(quotes_multiple(['600606', '002661', '600351']))
# -*- coding: UTF-8 -*-
# 更新每只股票的日K数据， 每个交易日运行一次

import time
import datetime
import json
import traceback
import pandas as pd
from qcinfo.log import task_log
from qcinfo import sina
from qcinfo import qcrepo
from qcinfo import D

logger = task_log()

# 是否为交易日
today = time.strftime("%Y-%m-%d", time.localtime())
if not D.is_trading(today):
    logger.info("Today: " + today + " is not trading day, exit the task.")

else:
    stocks = qcrepo.stocks()
    count = 0
    sum = 0
    codes = []
    for index, row in stocks.iterrows():
        if sum < 100:
            sum += 1
            codes.append(row["seccode"])
            continue
        try:
            quotess = sina.quotes_multiple(codes)
            for code, quotes in quotess.items():

                close = quotes["close"]  # 昨日收盘价
                timestamp = time.mktime(
                    datetime.datetime.strptime(str(quotes["date"])[0:10], "%Y-%m-%d").timetuple()) * 1000

                if float(quotes["volume"]) == 0:    # 停盘不更新
                    logger.info(code + " volume is 0, terminate update.")
                    continue

                now = quotes["now"]
                change = round(now - close, 2)
                percentage = round(change / close * 100, 2)
                pd.options.display.float_format = '{:.4f}'.format
                ds = [
                    timestamp,
                    quotes["open"],
                    now,    # 今日收盘价
                    quotes["high"],
                    quotes["low"],
                    quotes["money"],
                    quotes["volume"],
                    percentage,
                    change,
                    None
                ]
                qcrepo.append_quotes(quotes["code"], "d", json.dumps(ds))
                count += 1
                logger.info(str(count) + " update : " + quotes["code"] + " daily quotes successfully.")
        except:
            logger.error(traceback.format_exc())
            continue
        sum = 0
        codes = []




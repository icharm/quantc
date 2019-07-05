# -*- coding: UTF-8 -*-
# 更新每只股票的周K数据， 每周最后一个交易日运行一次

import time
import traceback
from qcinfo.log import task_log
from qcinfo import xueqiu
from qcinfo import qcrepo
from qcinfo import D

logger = task_log()


today = time.strftime("%Y-%m-%d", time.localtime())
# 是否为本周的最后一个交易日
if not D.islast_trading_day_week(today):
    logger.info("Today: " + today + " is not the last trading day of week, exit the task.")
else:
    # is last trading day of this week.
    stocks = qcrepo.stocks()
    count = 0
    for index, row in stocks.iterrows():
        try:
            code = row["seccode"]
            quotes = xueqiu.quotes(code, type="w", count=-1)
            timestamp = quotes["timestamp"][0]
            date = time.strftime("%Y-%m-%d", time.localtime(int(timestamp / 1000)))
            if date != today:  # 获取的行情不是今天的，放弃更新
                logger.info(code + " quotes timestamp is not today, is: " + date + ", give up the update.")
                continue
            if float(quotes["volume"][0]) == 0:  # 停盘不更新
                logger.info(code + " volume is 0, terminate update.")
                continue
            qcrepo.append_quotes(code, "w", quotes.iloc[0].to_json(orient="values"))
            count += 1
            logger.info(str(count) + " update : " + code + " weekly quotes successfully.")
        except:
            logger.error(traceback.format_exc())
            continue
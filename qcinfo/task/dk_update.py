# -*- coding: UTF-8 -*-
# 更新每只股票的日K数据， 每个交易日运行一次

import time
import traceback
from qcinfo.log import task_log
from qcinfo import xueqiu
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
    for index, row in stocks.iterrows():
        try:
            code = row["seccode"]
            quotes = xueqiu.quotes(code, type="d", count=-1)
            timestamp = quotes["timestamp"][0]
            date = time.strftime("%Y-%m-%d", time.localtime(int(timestamp / 1000)))
            if date != today:   # 获取的行情不是今天的，放弃更新
                logger.info(code + " quotes timestamp is not today, is: " + date + ", give up the update.")
                continue
            if float(quotes["volume"][0]) == 0:    # 停盘不更新
                logger.info(code + " volume is 0, terminate update.")
                continue
            qcrepo.append_quotes(code, "d", quotes.iloc[0].to_json(orient="values"))
            count += 1
            logger.info(str(count) + " update : " + code + " daily quotes successfully.")
        except:
            logger.error(traceback.format_exc())
            continue



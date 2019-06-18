# -*- coding: UTF-8 -*-
# 从xueqiu拉取所有股票至今的全部周K数据

import time
from qcinfo.log import task_log
import traceback
from qcinfo import xueqiu
from qcinfo import qcrepo

logger = task_log()

stocks = qcrepo.stocks()
count = 0
for index, row in stocks.iterrows():
    try:
        code = row["seccode"]
        quotes = xueqiu.quotes(code, type="w", count=-10000)
        quotes = quotes[0:-1]
        # 判断最后一条行情数据的日期是否是上周最后一个交易日
        times = quotes.iloc[-1, 0]
        date = time.strftime("%Y-%m-%d", time.localtime(times / 1000))
        if date != "2019-06-14":    # 手动修改为上一周的最后一个交易日
            logger.info("code: " + code + " last timestamp is: " + date + " not last working day, need to retry!")
        qcrepo.set_quotes(code, "w", quotes.to_json(orient="values"))
        count += 1
        logger.info(str(count) + " fetch " + str(code) + " week quotes success.")
        time.sleep(2)   # 防止太快 被封
    except:
        logger.error(traceback.format_exc())
        continue
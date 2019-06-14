# -*- coding: UTF-8 -*-
# 从cninfo获取所有股票基本信息

import time
import pandas as pd
from qcinfo import cninfo
from qcinfo import qcrepo
from qcinfo.log import task_log

logger = task_log()

category_dt = cninfo.categorys('1')
if category_dt == None:
    exit()
df = pd.DataFrame(columns=["seccode", "secname", "sdate", "mtype", "ptype"])
for i in [0, 1, 6, 7]: # 深证A 深证B 沪证A 沪证B
    stocks_dt = cninfo.stocks_under_category(category_dt['children'][i]['PARAM'], category_dt['children'][i]['API'])
    if stocks_dt == None:
        continue
    for stock in stocks_dt:
        df = df.append(
            pd.Series([stock["SECCODE"], stock['SECNAME'], str(stock['STARTDATE']), stock['F004V'], stock['F005V']], index=df.columns),
            ignore_index=True
        )
    time.sleep(5) # 防止太快 被封
qcrepo.set_stocks(df.to_json(orient="records"))
logger.info("Fetch successfully, found :" + str(len(df)))







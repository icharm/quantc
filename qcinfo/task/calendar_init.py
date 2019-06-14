# -*- coding: UTF-8 -*-
# 从szse抓取自2005-01以来的交易日历数据
import time
import datetime
import json
from qcinfo.log import task_log
import traceback
from qcinfo import szse
from qcinfo import qcrepo

logger = task_log()


date = datetime.datetime.today()
cals = []
try:
    for y in range(2005, 2020):
        for m in range(1, 13):
            date = date.replace(year=y, month=m)
            month = time.strftime('%Y-%m', date.timetuple())
            cal = szse.calendar_request(month)
            for index, value in cal.items():
                cals.append([value["date"], value["open"], value["weekday"]])
    file = qcrepo.wopen(qcrepo.dir + qcrepo.CALENDAR)
    file.write(json.dumps(cals))
    file.close()
    logger.info("Fetch calendar from szse successfully.")
except:
    logger.error(traceback.format_exc())







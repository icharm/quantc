# -*- coding: UTF-8 -*-
# Stock data fetch from website.
from basic import log
from . import xueqiu as XQ

logger = log.Log()

async def company_info_async(code):
    return await XQ.company_info_async(code)

# -*- coding: UTF-8 -*-
# Tencent stock data

import requests
# from tornado.httpclient import AsyncHTTPClient
# import re
from base import log
# from .model.quantc import SwStock
# from tornado import ioloop, queues
# import time
# import asyncio
# from datetime import timedelta

from sina import prefix

logger = log.Log()

# Synchronization methods
def daily_line_year(code, year='19'):
    url = 'http://data.gtimg.cn/flashdata/hushen/daily/' + year + '/' + prefix(code) + '.js?visitDstTime=1'
    response = requests.get(url)
    if response.status_code != 200:
        logger.error('Request error with stock code :' + code + ' ,response code: ' + response.status_code)
    dt = parse(response.text)
    return dt

def parse(str):
    lt = str.split('\n')[1:-1]
    dt = {}
    for item in lt:
        tmp = item.split(' ')



# if __name__ == '__main__':
    # io_loop = ioloop.IOLoop.current()
    # io_loop.run_sync(main)
daily_line_year('000750')











# q = queues.Queue()
#
#
#
# async def daily_line(code):
#     # 'http://data.gtimg.cn/flashdata/hushen/daily/17/' + code + '.js'
#     print(code + ' Start')
#     start = time.time()
#     # url = 'http://127.0.0.1:8000/sd/test?q=' + code
#     url = 'http://data.gtimg.cn/flashdata/hushen/daily/17/' + prefix(code) + '.js'
#     data = await AsyncHTTPClient().fetch(url)
#     end = time.time()
#     print(code + ' end ' + str(end - start))
#     return data
#
# async def run():
#     try:
#         stock = await q.get()
#         data = await daily_line(stock.seccode)
#         print(data)
#     finally:
#         q.task_done()
#
# async def worker():
#     while not q.empty():
#         await run()
#
# def main():
#     stocks = SwStock.select().where(SwStock.id <= 100)
#     tasks = []
#     for stock in stocks:
#         # q.put(stock)
#         tasks.append(daily_line(stock.seccode))
#     start = time.time()
#     # for _ in range(3):
#     #     await worker()
#     # await q.join(timeout=timedelta(seconds=300))
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(asyncio.gather(*tasks))
#     end = time.time()
#     print("Total time used: " + str(end-start))




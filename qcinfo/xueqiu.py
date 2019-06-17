# -*- coding: UTF-8 -*-
# Xueqiu.com stock data

import json
import pandas as pd
from .basic import *

base_url = "https://stock.xueqiu.com"

async def company_info_async(code):
    '''
        {
        "data": {
            "company": {
                "org_id": "02600276",
                "org_name_cn": "江苏恒瑞医药股份有限公司",
                "org_short_name_cn": "恒瑞医药",
                "org_name_en": "Jiangsu Hengrui Medicine Co.,Ltd.",
                "org_short_name_en": "HR",
                "main_operation_business": "药品研发、生产和销售",
                "operating_scope": "　　片剂（含抗肿瘤药）、口服溶液剂、混悬剂、原料药、精神药品、软胶囊剂（含抗肿瘤药）、冻干粉针剂（含抗肿瘤药）、粉针剂（抗肿瘤药、头孢菌素类）、吸入粉雾剂、口服混悬剂、口服乳剂、大容量注射剂（含多层共挤输液袋、含抗肿瘤药）、小容量注射剂（含抗肿瘤药、含非最终灭菌）、生物工程制品（聚乙二醇重组人粒细胞刺激因子注射液）、硬胶囊剂（含抗肿瘤药）、颗粒剂（抗肿瘤药）、粉雾剂、膜剂、凝胶剂、乳膏剂的制造；中药前处理及提取；一般化工产品的销售；自营和代理各类商品及技术的进出口业务，但国家限定公司经营或禁止进出口的商品和技术除外。",
                "district_encode": "320703",
                "org_cn_introduction": "江苏恒瑞医药股份有限公司是一家从事医药工业的公司,其主要生产产品包括了片剂、针剂、胶囊、粉针等制剂.\r\n　　公司是国内最大的抗肿瘤药、手术用药和造影剂的研究和生产基地之一。公司产品涵盖了抗肿瘤药、手术麻醉类用药、特色输液、造影剂、心血管药等众多领域，已形成比较完善的产品布局，其中抗肿瘤、手术麻醉、造影剂等领域市场份额在行业内名列前茅。报告期内，公司获得由中国化学制药工业协颁发的“2018中国化学制药行业工业企业综合实力百强”、“2018中国化学制药行业创新型优秀企业品牌”等众多荣誉。",
                "legal_representative": "孙飘扬",
                "general_manager": "周云曙",
                "secretary": "刘笑含",
                "established_date": 862156800000,
                "reg_asset": 4422814197,
                "staff_num": 21016,
                "telephone": "86-518-81220012",
                "postcode": "222000",
                "fax": "86-518-85453845",
                "email": "liuxiaohan@hrs.com.cn;shangqingming@hrs.com.cn",
                "org_website": "www.hrs.com.cn",
                "reg_address_cn": "江苏省连云港市连云区经济技术开发区黄河路38号",
                "reg_address_en": "",
                "office_address_cn": "江苏省连云港市连云区经济技术开发区昆仑山路7号",
                "office_address_en": "",
                "listed_date": 971798400000,
                "provincial_name": "江苏省",
                "actual_controller": "孙飘扬 (21.57%)",
                "classi_name": "民营企业",
                "pre_name_cn": null,
                "chairman": "孙飘扬",
                "executives_nums": 24,
                "actual_issue_vol": 40000000,
                "issue_price": 11.98,
                "actual_rc_net_amt": 466600000,
                "pe_after_issuing": 31.44,
                "online_success_rate_of_issue": 0.2572
            }
        },
        "error_code": 0,
        "error_description": ""
    }
    :param code: Stock code
    :return: Array item refer above json from api return
    '''
    url = base_url + "/v5/stock/f10/cn/company.json?symbol=" + prefix(code)
    content = await asyncrequest(url)
    if content is None:
        return None
    return json.loads(content)

def quotes(code, type="day"):
    '''
        "timestamp", 时间戳
        "volume", 成交量
        "open", 开盘价
        "high", 最高价
        "low", 最低价
        "close", 收盘价
        "chg", 涨跌额
        "percent", 涨跌幅
        "turnoverrate", 换手率
        "amount", 交易额
        "volume_post",
        "amount_post",
        "pe",
        "pb",
        "ps",
        "pcf",
        "market_capital",
        "balance",
        "hold_volume_cn",
        "hold_ratio_cn",
        "net_volume_cn",
        "hold_volume_hk",
        "hold_ratio_hk",
        "net_volume_hk"
    :param code:
    :param type:
    :return: dataframe
    '''
    url = base_url + "/v5/stock/chart/kline.json"
    param = {
        "symbol": prefix(code).upper(),
        "begin": 1560752836600,     # 开始时间戳
        "period": "day",
        "count": -10000,          # 往前的数量
        "indicator": "kline,pe,pb,ps,pcf,market_capital,agt,ggt,balance",
        "type": "normal"
    }
    params = ""
    for key, value in param.items():
        params += key + "=" + str(value) + "&"
    url = url + "?" + params
    header = {
        "Accept": "application/json, text/plain, */*",
        "Origin": "https://xueqiu.com",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        "Cookie": "xq_a_token=4ce3f2bb2f4cef9c2b6fd45cd157b8bb6c6c5bf6;"
    }
    content = requests.get(url, headers=header)
    arr = json.loads(content.text)
    arr1 = arr["data"]["item"]
    df = pd.DataFrame(data=arr1, columns=arr["data"]["column"])
    select = df[["timestamp", "open", "close", "high", "low", "amount", "volume", "percent", "chg", "turnoverrate"]]
    return select
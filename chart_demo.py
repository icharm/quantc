# -*- coding: UTF-8 -*- 
# Using hightchart to draw a html chart.
import pandas as pd
from cninfo.finance import BalanceSheet
from cninfo.common import IndustryStocks
from base import T
from base import log

log = log.Log(__name__)

def demo():
    '''
    绘制申万行业-乳品调味料分类下所有股票的负债表
    '''
    # 获取乳品调味料下所有股票基本信息
    stocks = IndustryStocks.sw_industry_stocks('S340402')
    sdf = pd.DataFrame(stocks)
    codelist = sdf['code'].values
    # 组装股票编码
    codes = ','.join(codelist)
    log.debug(codes)
    # 获取所有股票的所有资产负债表
    sheets = BalanceSheet.codes(codes)
    df = pd.DataFrame(sheets)
    #sel_df = df.loc[:, ['year', 'report_type_code', 'report_type', 'code', 'total_assets', 'payroll_payable']]
    #print(sel_df.code.unique())
    #sel_df = sel_df[sel_df.code == '002024']
    # 筛选所有合并类型为‘合并本期’的资产负债表
    sel_df = df[df.report_type_code == '071001']
    print(sel_df)
    #sel_df = sel_df.loc[:, ['year', 'total_assets']]
    T.draw(sel_df, xf='year', yf='total_liabilites', tf='name', title='Liabilites Chart')

demo()

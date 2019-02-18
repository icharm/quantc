# -*- coding: UTF-8 -*- 
import pandas as pd
class Day:
    """
        Trade day info formater class.
        Field list:
            date:                   日期
            is_first_day_week:      是否周初	    varchar	0-否；1-是；默认为0
            is_last_day_week:       是否周末	    varchar	0-否；1-是；默认为0
            is_first_day_month:     是否月初	    varchar	0-否；1-是；默认为0
            is_last_day_month:      是否月末	    varchar	0-否；1-是；默认为0
            is_trading_day:         是否交易日	    varchar	0-否；1-是；默认为0
            is_last_day_season:     是否季末	    varchar	0-否；1-是；默认为0
            is_last_day_halfyear:   是否半年末	    varchar	0-否；1-是；默认为0
            is_last_day_year:       是否年末	    varchar	0-否；1-是；默认为0
            is_bank_trading_day:    是否银行间交易日 varchar 0-否；1-是；默认为0
            previous_trading_day:   前一交易日	    date	
            next_trading_day:       后一交易日	    date
        """
    @staticmethod
    def parse(record):
        day = {}
        day['date'] = record['F001D']                   #F001D  日期	        date
        day['is_first_day_week'] = record['F002C']      #F002C  是否周初	    varchar	0-否；1-是；默认为0
        day['is_last_day_week'] = record['F003C']       #F003C  是否周末	    varchar	0-否；1-是；默认为0
        day['is_first_day_month'] = record['F004C']     #F004C  是否月初	    varchar	0-否；1-是；默认为0
        day['is_last_day_month'] = record['F005C']      #F005C	是否月末	    varchar	0-否；1-是；默认为0
        day['is_trading_day'] = record['F006C']         #F006C	是否交易日	    varchar	0-否；1-是；默认为0
        day['is_last_day_season'] = record['F007C']     #F007C	是否季末	    varchar	0-否；1-是；默认为0
        day['is_last_day_halfyear'] = record['F008C']   #F008C	是否半年末	    varchar	0-否；1-是；默认为0
        day['is_last_day_year'] = record['F009C']       #F009C  是否年末	    varchar	0-否；1-是；默认为0
        day['is_bank_trading_day'] = record['F010C']    #F010C	是否银行间交易日 varchar 0-否；1-是；默认为0
        day['previous_trading_day'] = record['F011D']   #F011D  前一交易日	    date	
        day['next_trading_day'] = record['F012D']       #F012D  后一交易日	    date
        return day
    
    @staticmethod
    def parses(records, count):
        if count <= 0:
            return ''
        elif count == 1:
            return Day.parse(records[0])
        else:
            day_list = []
            for record in records:
                day_list.append(Day.parse(record))
            return day_list

class Industry:
    '''
    Industry classification data formater handle class.
    Field list:
        parent_code: 父类编码 
        code: 类目编码
        name: 类目名称
    '''
    @staticmethod
    def parse(record):
        industry = {}
        industry['parent_code'] = record['PARENTCODE']      # PARENTCODE 父类编码	varchar	      
        industry['code'] = record['SORTCODE']               # SORTCODE 类目编码	varchar	
        industry['name'] = record['SORTNAME']               # SORTNAME 类目名称	varchar
        return industry                                     # Below field ignored
                                                            # F001V	类目名称（英文）	varchar	
                                                            # F002D	终止日期	DATE	
                                                            # F003V	行业类型编码	varchar	
                                                            # F004V	行业类型	varchar
    @staticmethod
    def parses(industries, count):
        if count <= 0:
            return ''
        elif count == 1:
            return Industry.parse(industries[0])
        else:
            industry_list = []
            for industry in industries:
                industry_list.append(Industry.parse(industry))
            return industry_list

class Region:
    '''
    Region classification data formater handle class.
    Field list:
        parent_code: 父类编码 
        code: 地区编码
        name: 地区名称
    '''
    @staticmethod
    def parse(record):
        region = {}         
        region['parent_code'] = record['PARENTCODE']    # PARENTCODE	父类编码	varchar	
        region['code'] = record['SORTCODE']             # SORTCODE	地区编码	varchar	
        region['name'] = record['SORTNAME']             # SORTNAME	地区名称	varchar	
        return region                                   # Below field ignored
                                                        # F001V	地区名称（英文）	varchar	
                                                        # F002D	终止日期	date
    @staticmethod
    def parses(regions, count):
        if count <= 0:
            return ''
        elif count == 1:
            return Region.parse(regions[0])
        else:
            region_list = []
            for region in regions:
                region_list.append(Region.parse(region))
            return region_list

class Stock:
    '''
    Stock basic info.
    Field list:
        code : 证券代码
        name : 证券简称
        org  :  机构名称
        type_code : 证券类别编码
        type : 证券类别
        market_code : 交易市场编码
        market : 交易市场
        start_date : 上市日期
        start_count : 初始上市数量
        attribute_code : 代码属性编码
        attribute : 代码属性
        status_code : 上市状态编码
        status :上市状态
    '''
    @staticmethod
    def parse_nc(records):
        '''
        Parse api return records to Stock object.
        '''
        stocks = []
        for record in records:
            stock = {}
            stock['code'] = record['SECCODE']
            stock['name'] = record['SECNAME']
            stocks.append(stock)
        return stocks

    @staticmethod
    def parse(stock):
        stock = {}           
        stock['code'] = stock['SECCODE']        # SECCODE	证券代码	varchar
        stock['name'] = stock['SECNAME']        # SECNAME	证券简称	varchar	
        stock['org'] = stock['ORGNAME']         # ORGNAME	机构名称	varchar	
        stock['type_code'] = stock['F002V']     # F002V	证券类别编码	varchar	
        stock['type'] = stock['F003V']          # F003V	证券类别	varchar	
        stock['market_code'] = stock['F004V']   # F004V	交易市场编码	varchar	
        stock['market'] = stock['F005V']        # F005V	交易市场	varchar	
        stock['start_date'] = stock['F006D']    # F006D	上市日期	datetime	
        stock['start_count'] = stock['F007N']   # F007N 初始上市数量	decimal	单位：股
        stock['attribute_code'] = stock['F008V']# F008V	代码属性编码	varchar	
        stock['attribute'] = stock['F009V']     # F009V	代码属性	varchar	
        stock['status_code'] = stock['F010V']   # F010V	上市状态编码	varchar	
        stock['status'] = stock['F011V']        # F011V	上市状态	varchar	
                                                # Below field ignored
                                                # F001V	拼音简称	varchar	
                                                # F012N	面值	decimal	单位：元
                                                # F013V	ISIN	varchar
        return stock
    
    @staticmethod
    def parses(stocks, count):
        if count <= 0:
            return ''
        elif count == 1:
            return Region.parse(stocks[0])
        else:
            stock_list = []
            for stock in stocks:
                stock_list.append(Region.parse(stock))
            return stock_list

class Corporation:
    '''
    Corporation basic info.
    Field list:

    '''
    @staticmethod
    def parse(record):
        corp = {}
        corp['org_id'] = record['ORGID']        # ORGID	机构ID	varchar	
        corp['org_name'] = record['ORGNAME']    # ORGNAME机构名称	varchar	
        #F001V	英文名称	varchar	
        #F002V	英文简称	varchar	
        #F003V	法人代表	varchar	
        #F004V	注册地址	varchar	
        #F005V	办公地址	varchar	
        #F006V	邮政编码	varchar	
        corp['reg_capital'] = record['F007N']   # F007N	注册资金	varchar	
        corp['currency_code'] = record['F008V'] # F008V	货币编码	varchar	
        corp['currency_name'] = record['F009V'] # F009V	货币名称	varchar	
        corp['setup_date'] = record['F010D']    # F010D	成立日期	DATE	
        corp['website'] = record['F011V']       # F011V	机构网址	varchar	
        #F012V	电子信箱	varchar	
        #F013V	联系电话	varchar	
        #F014V	联系传真	varchar	
        #F015V	主营业务	varchar	
        #F016V	经营范围	varchar	
        #F017V	机构简介/公司成立概况	varchar	
        #F018V	董事会秘书	varchar	
        #F019V	董秘联系电话	varchar	
        #F020V	董秘联系传真	varchar	
        #F021V	董秘电子邮箱	varchar	
        #F022V	证券事务代表	varchar	
        corp['status_code'] = record['F023V']   # F023V	上市状态编码	varchar	
        corp['status'] = record['F024V']        # F024V	上市状态	varchar	
        corp['province_code'] = record['F025V'] # F025V	所属省份编码	varchar	
        corp['province'] = record['F026V']      # F026V	所属省份	varchar	
        corp['city_code'] = record['F027V']     # F027V	所属城市编码	varchar	
        corp['city'] = record['F028V']          # F028V	所属城市	varchar	
        corp['sec_lv1_code'] = record['F029V']  # F029V	证监会一级行业编码	varchar	
        corp['sec_lv1_name'] = record['F030V']  # F030V	证监会一级行业名称	varchar	
        corp['sec_lv2_code'] = record['F031V']  # F031V	证监会二级行业编码	varchar	
        corp['sec_lv2_name'] = record['F032V']  # F032V	证监会二级行业名称	varchar	
        corp['sw_lv1_code'] = record['F033V']   # F033V	申万行业分类一级编码	varchar	
        corp['sw_lv1_name'] = record['F034V']   # F034V	申万行业分类一级名称	varchar	
        corp['sw_lv2_code'] = record['F035V']   # F035V	申万行业分类二级编码	varchar	
        corp['sw_lv2_name'] = record['F036V']   # F036V	申万行业分类二级名称	varchar	
        corp['sw_lv3_code'] = record['F037V']   # F037V	申万行业分类三级编码	varchar	
        corp['sw_lv3_name'] = record['F038V']   # F038V	申万行业分类三级名称	varchar	
        #F039V	会计师事务所	varchar	
        #F040V	律师事务所	varchar	
        #F041V	董事长	varchar	
        #F042V	总经理	varchar	
        #F043V	公司独立董事(现任)	varchar	多名
        corp['index_selected'] = record['F044V']    # F044V	入选指数	varchar	多个
        corp['latest_report_date'] = record['F045V'] #F045V	最新报告预约日期	varchar	
        #F046V	保荐机构	varchar	多个
        #F047V	主承销商	varchar	
        corp['code'] = record['SECCODE']        # SECCODE	股票代码	varchar	
        corp['name'] = record['SECNAME']        # SECNAME	股票简称	varchar
        return corp

    @staticmethod
    def parses(records, count):
        if count <= 0:
            return ''
        elif count == 1:
            return Corporation.parse(records[0])
        else:
            corp_list = []
            for corp in records:
                corp_list.append(Corporation.parse(corp))
            return corp_list

class BalanceSheet:
    '''
    Balance sheet data.
    '''
    @staticmethod
    def parse(record):
        sheet = {}
        sheet['name'] = record['SECNAME'] # SECNAME	证券简称	varchar	
        sheet['code'] = record['SECCODE'] # SECCODE	证券代码	varchar	
        sheet['org'] = record['ORGNAME']  # ORGNAME	机构名称	varchar	
        sheet['report_date'] = record['DECLAREDATE'] # DECLAREDATE	公告日期	date	
        sheet['end_date'] = record['ENDDATE'] # ENDDATE	截止日期	date	
        sheet['year'] = record['F001D'] # F001D	报告年度	date	
        sheet['report_type_code'] = record['F002V'] # F002V	合并类型编码	varchar	
        sheet['report_type'] = record['F003V'] # F003V	合并类型	varchar	
        # F004V	报表来源编码	varchar	
        # F005V	报表来源	varchar	
        sheet['monetay_funds'] = record['F006N'] # F006N	货币资金(现金储备)	decimal	单位：元 
        sheet['financial_assets'] = record['F007N'] # F007N	以公允价值计量且其变动计入当期损益的金融资产	decimal	单位：元
        sheet['bill_receivable']  = record['F008N'] # F008N	应收票据	decimal	单位：元
        sheet['accounts_receivable'] = record['F009N'] # F009N	应收账款	decimal	单位：元
        sheet['advance_payment'] = record['F010N'] # F010N	预付款项(欠账)	decimal	单位：元
        sheet['other_receivable'] = record['F011N']  # F011N	其他应收款	decimal	单位：元
        sheet['affiliated_company_receivable'] = record['F012N'] # F012N	应收关联公司(母公司or子公司)款	decimal	单位：元
        sheet['interest_receivable'] = record['F013N'] # F013N	应收利息	decimal	单位：元
        sheet['dividend_receivable'] = record['F014N'] # F014N	应收股利	decimal	单位：元
        sheet['inventory'] = record['F015N'] # F015N	存货(库存)	decimal	单位：元
        sheet['expendable_biological_assets'] = record['F016N'] # F016N	其中：消耗性生物资产	decimal	单位：元
        sheet['illiquid_assets_expried_nextyear'] = record['F017N'] # F017N	一年内到期的非流动资产	decimal	单位：元
        sheet['other_current_assets'] = record['F018N'] # F018N	其他流动资产	decimal	单位：元
        sheet['total_current_assets'] = record['F019N'] # F019N	流动资产合计	decimal	单位：元
        sheet['financial_assets_salability'] = record['F020N'] # F020N	可供出售金融资产	decimal	单位：元
        sheet['held_maturity_investment'] = record['F021N'] # F021N	持有至到期投资	decimal	单位：元
        sheet['long_term_receviables'] = record['F022N'] # F022N	长期应收款	decimal	单位：元
        sheet['long_term_stock_investment'] = record['F023N'] # F023N	长期股权投资	decimal	单位：元
        sheet['real_estate_investment'] = record['F024N'] # F024N	投资性房地产	decimal	单位：元
        sheet['fixed_assets'] = record['F025N'] # F025N	固定资产	decimal	单位：元
        sheet['construction_in_process'] = record['F026N'] # F026N	在建工程(支出)	decimal	单位：元
        sheet['engineer_material'] = record['F027N'] # F027N	工程物资	decimal	单位：元
        sheet['fixed_assets_disposal'] = record['F028N'] # F028N	固定资产清理	decimal	单位：元
        sheet['productive_biological_assets'] = record['F029N'] # F029N	生产性生物资产	decimal	单位：元
        sheet['oil_gas_assets'] = record['F030N'] # F030N	油气资产	decimal	单位：元
        sheet['intangible_assets'] = record['F031N'] # F031N	无形资产	decimal	单位：元
        sheet['development_expenditure'] = record['F032N'] # F032N	开发支出	decimal	单位：元
        sheet['business_reputation'] = record['F033N'] # F033N	商誉	decimal	单位：元
        sheet['long_term_deferred_expenses'] = record['F034N'] # F034N	长期待摊费用	decimal	单位：元
        sheet['deferred_income_tax_assets'] = record['F035N'] # F035N	递延所得税资产	decimal	单位：元
        sheet['other_non_current_assets'] = record['F036N'] # F036N	其他非流动资产	decimal	单位：元
        sheet['total_non_current_assets'] = record['F037N'] # F037N	非流动资产合计	decimal	单位：元
        sheet['total_assets'] = record['F038N'] # F038N	资产总计	decimal	单位：元
        sheet['short_term_borrowing'] = record['F039N'] # F039N	短期借款	decimal	单位：元
        sheet['financial_liabilities'] = record['F040N'] # F040N	以公允价值计量且其变动计入当期损益的金融负债	decimal	单位：元
        sheet['bill_payable'] = record['F041N'] # F041N	应付票据	decimal	单位：元
        sheet['accounts_payable'] = record['F042N'] # F042N	应付账款	decimal	单位：元
        sheet['accounts_received_advance'] = record['F043N'] # F043N	预收款项	decimal	单位：元
        sheet['payroll_payable'] = record['F044N'] # F044N	应付职工薪酬	decimal	单位：元
        sheet['taxes_payable'] = record['F045N'] # F045N	应交税费	decimal	单位：元
        sheet['interest_payable'] = record['F046N'] # F046N	应付利息	decimal	单位：元
        sheet['dividend_payable'] = record['F047N'] # F047N	应付股利	decimal	单位：元
        sheet['other_payable'] = record['F048N'] # F048N	其他应付款	decimal	单位：元
        sheet['affiliated_company_payable'] = record['F049N'] # F049N	应付关联公司款	decimal	单位：元
        sheet['illiquid_liabilities_expried_nextyear'] = record['F050N'] # F050N	一年内到期的非流动负债	decimal	单位：元
        sheet['other_current_liability'] = record['F051N'] # F051N	其他流动负债	decimal	单位：元
        sheet['total_current_liability'] = record['F052N'] # F052N	流动负债合计	decimal	单位：元
        sheet['long_term_borrowing'] = record['F053N'] # F053N	长期借款	decimal	单位：元
        sheet['bond_payable'] = record['F054N'] # F054N	应付债券	decimal	单位：元
        sheet['long_term_payable'] = record['F055N'] # F055N	长期应付款	decimal	单位：元
        sheet['special_payable'] = record['F056N'] # F056N	专项应付款	decimal	单位：元
        sheet['estimated_liabilites'] = record['F057N'] # F057N	预计负债	decimal	单位：元
        sheet['deferred_income_tax_liabilites'] = record['F058N'] # F058N	递延所得税负债	decimal	单位：元
        sheet['other_illiquid_liabilites'] = record['F059N'] # F059N	其他非流动负债	decimal	单位：元
        sheet['total_illiquid_liabilites'] = record['F060N'] # F060N	非流动负债合计	decimal	单位：元
        sheet['total_liabilites'] = record['F061N'] # F061N	负债合计	decimal	单位：元
        sheet['paid_in_capital'] = record['F062N'] # F062N	实收资本（或股本）	decimal	单位：元
        sheet['additional_paid_in_capital'] = record['F063N'] # F063N	资本公积	decimal	单位：元
        sheet['features_surplus'] = record['F064N'] # F064N	盈余公积	decimal	单位：元
        sheet['special_reserves'] = record['F072N'] # F072N	专项储备	decimal	单位：元
        sheet['treasury_share'] = record['F066N'] # F066N	减：库存股	decimal	单位：元
        sheet['generic_risk_reserves'] = record['F076N'] # F076N	一般风险准备	decimal	单位：元
        sheet['undistributed_profits'] = record['F065N'] # F065N	未分配利润	decimal	单位：元
        sheet['mother_company_interest'] = record['F073N'] # F073N	归属于母公司所有者权益	decimal	单位：元
        sheet['minority_stock_holder_interest'] = record['F067N'] # F067N	少数股东权益	decimal	单位：元
        sheet['translation_foreign_statements'] = record['F068N'] # F068N	外币报表折算价差	decimal	单位：元
        sheet['income_abnormal_project'] = record['F069N'] # F069N	非正常经营项目收益调整	decimal	单位：元
        sheet['total_investors_equity'] = record['F070N'] # F070N	所有者权益（或股东权益）合计	decimal	单位：元
        sheet['total_equity_liabilites'] = record['F071N'] # F071N	负债和所有者（或股东权益）合计	decimal	单位：元
        sheet['remark'] = record['MEMO'] # MEMO	备注	varchar	
        sheet['other_comprehensive_income'] = record['F074N'] # F074N	其他综合收益	decimal	单位：元
        sheet['deferred_illiquid_liabilites'] = record['F075N'] # F075N	递延收益-非流动负债	decimal	单位：元
        sheet['deposit_reservation'] = record['F077N'] # F077N	结算备付金	decimal	单位：元
        sheet['lendings_funds'] = record['F078N'] # F078N	拆出资金	decimal	单位：元
        sheet['lendings_liquid_funds'] = record['F079N'] # F079N	发放贷款及垫款-流动资产	decimal	单位：元
        sheet['derivative_assets'] = record['F080N'] # F080N	衍生金融资产	decimal	单位：元
        sheet['insurance_receivable'] = record['F081N'] # F081N	应收保费(保险公司)	decimal	单位：元
        sheet['reinsurance_accounts_receivable'] = record['F082N'] # F082N	应收分保账款	decimal	单位：元
        sheet['contract_reserve_receivable'] = record['F083N'] # F083N	应收分保合同准备金	decimal	单位：元
        sheet['buy_sale_financial_assets'] = record['F084N'] # F084N	买入返售金融资产	decimal	单位：元
        sheet['hold_for_sale_assets'] = record['F085N'] # F085N	划分为持有待售的资产	decimal	单位：元
        sheet['lendings_illiquid_funds'] = record['F086N'] # F086N	发放贷款及垫款-非流动资产	decimal	单位：元
        sheet['borrowing_from_central_bank'] = record['F087N'] # F087N	向中央银行借款(银行)	decimal	单位：元
        sheet['interbank_and_absorption'] = record['F088N'] # F088N	吸收存款及同业存放(银行)	decimal	单位：元
        sheet['loans_from_bank'] = record['F089N'] # F089N	拆入资金	decimal	单位：元
        sheet['derivative_liabilites'] = record['F090N'] # F090N	衍生金融负债	decimal	单位：元
        sheet['sold_repurchase_financial_assets'] = record['F091N'] # F091N	卖出回购金融资产款	decimal	单位：元
        sheet['fees_commissions_payable'] = record['F092N'] # F092N	应付手续费及佣金	decimal	单位：元
        sheet['reinsurance_accounts_payable'] = record['F093N'] # F093N	应付分保账款	decimal	单位：元
        sheet['insurance_contract_reserve'] = record['F094N'] # F094N	保险合同准备金	decimal	单位：元
        sheet['acting_trading_securities'] = record['F095N'] # F095N	代理买卖证券款(证券公司)	decimal	单位：元
        sheet['acting_underwriting_securities'] = record['F096N'] # F096N	代理承销证券款	decimal	单位：元
        sheet['hold_for_sale_liabilites'] = record['F097N'] # F097N	划分为持有待售的负债	decimal	单位：元
        sheet['estimated_current_liabilites'] = record['F098N'] # F098N	预计负债-流动负债	decimal	单位：元
        sheet['deferred_current_liabilites'] = record['F099N'] # F099N	递延收益-流动负债	decimal	单位：元
        sheet['preferred_illiquid_liabilites'] = record['F100N'] # F100N	其中：优先股-非流动负债	decimal	单位：元
        sheet['perpetual_debt_illiquid_liabilites'] = record['F101N'] # F101N	永续债-非流动负债	decimal	单位：元
        sheet['long_term_payroll'] = record['F102N'] # F102N	长期应付职工薪酬	decimal	单位：元
        sheet['other_equity_instruments'] = record['F103N'] # F103N	其他权益工具	decimal	单位：元
        sheet['preferred_investory_equity'] = record['F104N'] # F104N	其中：优先股-所有者权益	decimal	单位：元
        sheet['perpetual_debt_investory_equity'] = record['F105N'] # F105N	永续债-所有者权益	decimal	单位：元
        return sheet

    @staticmethod
    def parses(records, count):
        if count <= 0:
            return ''
        elif count == 1:
            return pd.Series(BalanceSheet.parse(records[0]))
        else:
            sheet_list = []
            for sheet in records:
                sheet_list.append(BalanceSheet.parse(sheet))
            return pd.DataFrame(sheet_list)

class ProfitSheet:

    @staticmethod
    def parse(record):
        sheet = {}
        sheet['code'] = record['SECCODE']                   # SECCODE	证券代码	varchar	
        sheet['name'] = record['SECNAME']                   # SECNAME	证券简称	varchar	
        sheet['org'] = record['ORGNAME']                    # ORGNAME	机构名称	varchar	
        sheet['rdate'] = record['DECLAREDATE']              # DECLAREDATE	公告日期	date	
        sheet['sdate'] = record['STARTDATE']                # STARTDATE	开始日期	date	
        sheet['edate'] = record['ENDDATE']                  # ENDDATE	截止日期	date	
        sheet['year'] = record['F001D']                     # F001D	报告年度	date	
        sheet['tcode'] = record['F002V']                    # F002V	合并类型编码	varchar	
        sheet['type'] = record['F003V']                     # F003V	合并类型	varchar	
        sheet['scode'] = record['F004V']                    # F004V	报表来源编码	varchar	
        sheet['source'] = record['F005V']                   # F005V	报表来源	varchar	
        sheet['total_operating_income'] = record['F035N']   # F035N	一、营业总收入	decimal	单位：元
        sheet['operating_income'] = record['F006N']         # F006N	其中：营业收入	decimal	单位：元
        sheet['total_operating_costs'] = record['F036N']    # F036N	二、营业总成本	decimal	单位：元
        sheet['operating_costs'] = record['F007N']          # F007N	其中：营业成本	decimal	单位：元
        sheet['business_taxes_surcharges'] = record['F008N'] # F008N	营业税金及附加	decimal	单位：元
        sheet['selling_fee'] = record['F009N']              # F009N	销售费用	decimal	单位：元
        sheet['management_fee'] = record['F010N']           # F010N	管理费用	decimal	单位：元
        sheet['exporing_fee'] = record['F011N']             # F011N	堪探费用	decimal	单位：元
        sheet['financing_fee'] = record['F012N']            # F012N	财务费用	decimal	单位：元
        sheet['assets_impairment_loss'] = record['F013N']   # F013N	资产减值损失	decimal	单位：元
        sheet['fair_value_change_income'] = record['F014N'] # F014N	加：公允价值变动净收益	decimal	单位：元
        sheet['investment_income'] = record['F015N']        # F015N	投资收益	decimal	单位：元
        sheet['associates_investment_income'] = record['F016N'] # F016N	其中：对联营企业和合营企业的投资收益	decimal	单位：元
        sheet['exchange_income'] = record['F037N']          # F037N	汇兑收益	decimal	单位：元
        sheet['other_operating'] = record['F017N']          # F017N	影响营业利润的其他科目	decimal	单位：元
        sheet['selling_profit'] = record['F018N']           # F018N	三、营业利润	decimal	单位：元
        sheet['subsidize_income'] = record['F019N']         # F019N	加：补贴收入	decimal	单位：元
        sheet['non_operating_income'] = record['F020N']     # F020N	营业外收入	decimal	单位：元
        sheet['non_operating_expenditure'] = record['F021N'] # F021N	减：营业外支出	decimal	单位：元
        sheet['illiquid_assets_disposal_loss'] = record['F022N'] # F022N	其中：非流动资产处置损失	decimal	单位：元
        sheet['other_profit'] = record['F023N']             # F023N	加：影响利润总额的其他科目	decimal	单位：元
        sheet['total_profit'] = record['F024N']             # F024N	四、利润总额	decimal	单位：元
        sheet['income_tax'] = record['F025N']               # F025N	减：所得税	decimal	单位：元
        sheet['other_net_profit'] = record['F026N']         # F026N	加：影响净利润的其他科目	decimal	单位：元
        sheet['net_profit'] = record['F027N']               # F027N	五、净利润	decimal	单位：元
        sheet['mother_company_profit'] = record['F028N']    # F028N	归属于母公司所有者的净利润	decimal	单位：元
        sheet['minority_interest_income'] = record['F029N'] # F029N	少数股东损益	decimal	单位：元
        sheet['base_income_share'] = record['F031N']        # F031N	（一）基本每股收益	decimal	
        sheet['diluted_income_share'] = record['F032N']     # F032N	（二）稀释每股收益	decimal	
        sheet['other_comprehensive_income'] = record['F038N'] # F038N	七、其他综合收益	decimal	单位：元
        sheet['total_comprehensive_income'] = record['F039N'] # F039N	八、综合收益总额	decimal	单位：元
        sheet['belong_mother_income'] = record['F040N']     # F040N	其中：归属于母公司	decimal	单位：元
        sheet['belong_minority_income'] = record['F041N']   # F041N	其中：归属于少数股东	decimal	单位：元
        sheet['remark'] = record['MEMO']                    # MEMO	备注	varchar	
        sheet['interest_income'] = record['F033N']          # F033N	利息收入	decimal	单位：元
        sheet['insurance_income'] = record['F034N']         # F034N	已赚保费	decimal	单位：元
        sheet['fee_commission_income'] = record['F042N']    # F042N	手续费及佣金收入	decimal	单位：元
        sheet['interest_expense'] = record['F043N']         # F043N	利息支出	decimal	单位：元
        sheet['fee_commission_expense'] = record['F044N']   # F044N	手续费及佣金支出	decimal	单位：元
        sheet['surrender'] = record['F045N']                # F045N	退保金	decimal	单位：元
        sheet['compensation_expense'] = record['F046N']     # F046N	赔付支出净额	decimal	单位：元
        sheet['insurance_contract_reserve'] = record['F047N'] # F047N	提取保险合同准备金净额	decimal	单位：元
        sheet['insurance_dividend_expense'] = record['F048N'] # F048N	保单红利支出	decimal	单位：元
        sheet['amortized_insurance_expense'] = record['F049N'] # F049N	分保费用	decimal	单位：元
        sheet['illiquid_disposal_income'] = record['F050N'] # F050N	其中：非流动资产处置利得	decimal	单位：元
        sheet['other_income'] = record['F051N']             # F051N	其他收益	decimal	单位：元
        return sheet

    @staticmethod
    def parses(records, count):
        if count <= 0:
            return ''
        elif count == 1:
            return pd.Series(ProfitSheet.parse(records[0]))
        else:
            sheet_list = []
            for sheet in records:
                sheet_list.append(ProfitSheet.parse(sheet))
            return pd.DataFrame(sheet_list)

class CashFlow:
    @staticmethod
    def parse(record):
        sheet = []
        sheet['name'] = record['SECNAME'] # SECNAME	证券简称	varchar	
        sheet['code'] = record['SECCODE'] # SECCODE	证券代码	varchar	
        sheet['org'] = record['ORGNAME'] # ORGNAME	机构名称	varchar	
        sheet['rdate'] = record['DECLAREDATE'] # DECLAREDATE	公告日期	date	
        sheet['sdate'] = record['STARTDATE'] # STARTDATE	开始日期	date	
        sheet['edate'] = record['ENDDATE'] # ENDDATE	截止日期	date	
        sheet['year'] = record['F001D'] # F001D	报告年度	date	
        sheet['tcode'] = record['F002V'] # F002V	合并类型编码	varchar	
        sheet['type'] = record['F003V'] # F003V	合并类型	varchar	
        sheet['scode'] = record['F004V'] # F004V	报表来源编码	varchar	
        sheet['source'] = record['F005V'] # F005V	报表来源	varchar	
        sheet['sale_cash'] = record['F006N'] # F006N	销售商品、提供劳务收到的现金	decimal	单位：元 +
        sheet['tax_ret'] = record['F007N'] # F007N	收到的税费返还	decimal	单位：元 +
        sheet['other_cash'] = record['F008N'] # F008N	收到其他与经营活动有关的现金	decimal	单位：元 +
        sheet['subtotal_cash_inflow'] = record['F009N'] # F009N	经营活动现金流入小计	decimal	单位：元 *
        sheet['goods'] = record['F010N'] # F010N	购买商品、接受劳务支付的现金	decimal	单位：元 -
        sheet['salary'] = record['F011N'] # F011N	支付给职工以及为职工支付的现金	decimal	单位：元 -
        sheet['taxs'] = record['F012N'] # F012N	支付的各项税费	decimal	单位：元 -
        sheet['others'] = record['F013N'] # F013N	支付其他与经营活动有关的现金	decimal	单位：元 -
        sheet['subtotal_cash_outflow'] = record['F014N'] # F014N	经营活动现金流出小计	decimal	单位：元 -
        sheet['net_operations'] = record['F015N'] # F015N	经营活动产生的现金流量净额	decimal	单位：元 *
        sheet['receive_investment'] = record['F016N'] # F016N	收回投资收到的现金	decimal	单位：元 +
        sheet['income_investment'] = record['F017N'] # F017N	取得投资收益收到的现金	decimal	单位：元 +
        sheet['net_disposal_assets'] = record['F018N'] # F018N	处置固定资产、无形资产和其他长期资产收回的现金净额	decimal	单位：元 +
        sheet['net_disposal_unit'] = record['F019N'] # F019N	处置子公司及其他营业单位收到的现金净额	decimal	单位：元 +
        sheet['others_investment'] = record['F020N'] # F020N	收到其他与投资活动有关的现金	decimal	单位：元 +
        sheet['subtotal_investment_in'] = record['F021N'] # F021N	投资活动现金流入小计	decimal	单位：元 *
        sheet['pay_assets'] = record['F022N'] # F022N	购建固定资产、无形资产和其他长期资产支付的现金	decimal	单位：元 -
        sheet['pay_investment'] = record['F023N'] # F023N	投资支付的现金	decimal	单位：元 -
        sheet['net_increase_loans'] = record['F075N'] # F075N	质押贷款净增加额	decimal	单位：元 +
        sheet['net_receive_unit'] = record['F024N'] # F024N	取得子公司及其他营业单位支付的现金净额	decimal	单位：元 +
        sheet['pay_others_investment'] = record['F025N'] # F025N	支付其他与投资活动有关的现金	decimal	单位：元 -
        sheet['subtotal_investment_out'] = record['F026N'] # F026N	投资活动现金流出小计	decimal	单位：元 -
        sheet['net_investment'] = record['F027N'] # F027N	投资活动产生的现金流量净额	decimal	单位：元
        sheet['investment_in'] = record['F028N'] # F028N	吸收投资收到的现金	decimal	单位：元
        sheet['borrow_in'] = record['F029N'] # F029N	取得借款收到的现金	decimal	单位：元
        sheet['bonds_in'] = record['F076N'] # F076N	发行债券收到的现金	decimal	单位：元
        sheet['others_fundraising_in'] = record['F030N'] # F030N	收到其他与筹资活动有关的现金	decimal	单位：元
        sheet['subtotal_fundraising_in'] = record['F031N'] # F031N	筹资活动现金流入小计	decimal	单位：元
        sheet['repay_loan'] = record['F032N'] # F032N	偿还债务支付的现金	decimal	单位：元
        sheet['pay_dividends_profits_interest'] = record['F033N'] # F033N	分配股利、利润或偿付利息支付的现金	decimal	单位：元
        sheet['pay_fundraising'] = record['F034N'] # F034N	支付其他与筹资活动有关的现金	decimal	单位：元
        sheet['subtotal_fundraising_out'] = record['F035N'] # F035N	筹资活动现金流出小计	decimal	单位：元
        sheet['net_fundraising'] = record['F036N'] # F036N	筹资活动产生的现金流量净额	decimal	单位：元
        sheet['effect_exchange_rate'] = record['F037N'] # F037N	四、汇率变动对现金的影响	decimal	单位：元
        sheet['effect_others'] = record['F038N'] # F038N	四(2)、其他原因对现金的影响	decimal	单位：元
        sheet['net_increase_cash'] = record['F039N'] # F039N	五、现金及现金等价物净增加额	decimal	单位：元
        sheet[''] = record['F040N'] # F040N	期初现金及现金等价物余额	decimal	单位：元
        sheet[''] = record['F041N'] # F041N	期末现金及现金等价物余额	decimal	单位：元
        sheet[''] = record['F044N'] # F044N	净利润	decimal	单位：元
        sheet[''] = record['F045N'] # F045N	加：资产减值准备	decimal	单位：元
        sheet[''] = record['F046N'] # F046N	固定资产折旧、油气资产折耗、生产性生物资产折旧	decimal	单位：元
        sheet[''] = record['F047N'] # F047N	无形资产摊销	decimal	单位：元
        sheet[''] = record['F048N'] # F048N	长期待摊费用摊销	decimal	单位：元
        sheet[''] = record['F049N'] # F049N	处置固定资产、无形资产和其他长期资产的损失	decimal	单位：元
        sheet[''] = record['F050N'] # F050N	固定资产报废损失	decimal	单位：元
        sheet[''] = record['F051N'] # F051N	公允价值变动损失	decimal	单位：元
        sheet[''] = record['F052N'] # F052N	财务费用	decimal	单位：元
        sheet[''] = record['F053N'] # F053N	投资损失	decimal	单位：元
        sheet[''] = record['F054N'] # F054N	递延所得税资产减少	decimal	单位：元
        sheet[''] = record['F055N'] # F055N	递延所得税负债增加	decimal	单位：元
        sheet[''] = record['F056N'] # F056N	存货的减少	decimal	单位：元
        sheet[''] = record['F057N'] # F057N	经营性应收项目的减少	decimal	单位：元
        sheet[''] = record['F058N'] # F058N	经营性应付项目的增加	decimal	单位：元
        sheet[''] = record['F059N'] # F059N	其他	decimal	单位：元
        sheet[''] = record['F060N'] # F060N	经营活动产生的现金流量净额2	decimal	单位：元
        sheet[''] = record['F062N'] # F062N	债务转为资本	decimal	单位：元
        sheet[''] = record['F063N'] # F063N	一年内到期的可转换公司债券	decimal	单位：元
        sheet[''] = record['F064N'] # F064N	融资租入固定资产	decimal	单位：元
        sheet[''] = record['F066N'] # F066N	现金的期末余额	decimal	单位：元
        sheet[''] = record['F067N'] # F067N	减：现金的期初余额	decimal	单位：元
        sheet[''] = record['F068N'] # F068N	加：现金等价物的期末余额	decimal	单位：元
        sheet[''] = record['F069N'] # F069N	减：现金等价物的期初余额	decimal	单位：元
        sheet[''] = record['F070N'] # F070N	加：其他原因对现金的影响2	decimal	单位：元
        sheet[''] = record['F071N'] # F071N	现金及现金等价物净增加额2	decimal	单位：元
        sheet[''] = record['F072N'] # F072N	客户存款和同业存放款项净增加额	decimal	单位：元
        sheet[''] = record['F073N'] # F073N	向中央银行借款净增加额	decimal	单位：元
        sheet[''] = record['F074N'] # F074N	向其他金融机构拆入资金净增加额	decimal	单位：元
        sheet[''] = record['F077N'] # F077N	收到原保险合同保费取得的现金	decimal	单位：元
        sheet[''] = record['F078N'] # F078N	收到再保险业务现金净额	decimal	单位：元
        sheet[''] = record['F079N'] # F079N	保户储金及投资款净增加额	decimal	单位：元
        sheet[''] = record['F080N'] # F080N	处置以公允价值计量且其变动计入当期损益的金融资产净增加额	decimal	单位：元
        sheet[''] = record['F081N'] # F081N	收取利息、手续费及佣金的现金	decimal	单位：元
        sheet[''] = record['F082N'] # F082N	拆入资金净增加额	decimal	单位：元
        sheet[''] = record['F083N'] # F083N	回购业务资金净增加额	decimal	单位：元
        sheet[''] = record['F084N'] # F084N	客户贷款及垫款净增加额	decimal	单位：元
        sheet[''] = record['F085N'] # F085N	存放中央银行和同业款项净增加额	decimal	单位：元
        sheet[''] = record['F086N'] # F086N	支付原保险合同赔付款项的现金	decimal	单位：元
        sheet[''] = record['F087N'] # F087N	支付利息、手续费及佣金的现金	decimal	单位：元
        sheet[''] = record['F088N'] # F088N	支付保单红利的现金	decimal	单位：元
        sheet[''] = record['F089N'] # F089N	其中：子公司吸收少数股东投资收到的现金	decimal	单位：元
        sheet[''] = record['F090N'] # F090N	其中：子公司支付给少数股东的股利、利润	decimal	单位：元
        sheet[''] = record['F091N'] # F091N	投资性房地产的折旧及摊销	decimal	单位：元
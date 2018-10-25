# -*- coding: UTF-8 -*- 

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
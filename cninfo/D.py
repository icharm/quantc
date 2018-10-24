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
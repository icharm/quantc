# -*- coding: UTF-8 -*-

import datetime
from peewee import *
from basic import config
from basic import log

logger = log.Log()
db = SqliteDatabase(config.db_default)
# db = MySQLDatabase('qcinfo', user=config.db_username, password=config.db_password, host=config.db_address, port=config.db_port)

class SwStock(Model):
    seccode = CharField()
    secname = CharField()
    startdate = DateField()
    sw1 = CharField()
    sw2 = CharField()
    sw3 = CharField()
    sw = TextField()
    updated = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db

class HammerShape(Model):
    seccode = CharField()
    secname = CharField()
    type = CharField(null=True)      # day, week, month line hammer shape
    trend_before = IntegerField(null=True)   # rise 1 or drop -1
    color = IntegerField()  # rise 1 or drop -1
    ratio = DoubleField()   # entity ratio
    lratio = DoubleField()  # line header ratio
    date = DateField()      # trade date
    close = DoubleField()   # close price.
    trend_after = IntegerField(null=True)    # rise 1 or drop -1
    range_day1 = DoubleField(null=True)      # after one day range of pice change.
    range_day2 = DoubleField(null=True)
    range_day3 = DoubleField(null=True)
    range_day4 = DoubleField(null=True)
    range_day5 = DoubleField(null=True)
    range_week1 = DoubleField(null=True)     # after one week range of pice change.
    range_week2 = DoubleField(null=True)
    range_week3 = DoubleField(null=True)
    range_week4 = DoubleField(null=True)
    range_month = DoubleField(null=True)
    score_s = DoubleField(null=True)  # hammer shape score
    score_p = DoubleField(null=True)  # prediction score
    updated = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db

class TradeCalendar(Model):
    month = CharField(unique=True)
    calendar = TextField()
    updated = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db

class HammerShapeWeek(Model):
    seccode = CharField()
    secname = CharField()
    type = CharField(null=True)      # day, week, month line hammer shape
    trend_before = IntegerField(null=True)   # rise 1 or drop -1
    color = IntegerField()  # rise 1 or drop -1
    ratio = DoubleField()   # entity ratio
    lratio = DoubleField()  # line header ratio
    date = DateField()      # trade date
    close = DoubleField()   # close price.
    trend_after = IntegerField(null=True)    # rise 1 or drop -1
    week1 = DoubleField(null=True)      # after one day range of pice change.
    week2 = DoubleField(null=True)
    week3 = DoubleField(null=True)
    month1 = DoubleField(null=True)
    week5 = DoubleField(null=True)
    week6 = DoubleField(null=True)     # after one week range of pice change.
    week7 = DoubleField(null=True)
    month2 = DoubleField(null=True)
    score_s = DoubleField(null=True)  # hammer shape score
    score_p = DoubleField(null=True)  # prediction score
    updated = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db

class VenusShape(Model):
    seccode = CharField()
    secname = CharField()
    type = CharField()  # day, week, month line hammer shape
    trend_before = IntegerField(null=True)  # rise 1 or drop -1
    color = IntegerField(null=True)  # rise 1 or drop -1
    date = DateField()  # trade date
    close = DoubleField()  # close price.
    trend_after = IntegerField(null=True)  # rise 1 or drop -1
    d1 = DoubleField(null=True)
    d2 = DoubleField(null=True)
    d3 = DoubleField(null=True)
    d4 = DoubleField(null=True)
    d5 = DoubleField(null=True)
    d6 = DoubleField(null=True)
    d7 = DoubleField(null=True)
    d8 = DoubleField(null=True)
    d9 = DoubleField(null=True)
    d10 = DoubleField(null=True)
    score_s = DoubleField(null=True)
    score_p = DoubleField(null=True)
    updated = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db

tables = [SwStock, HammerShape, TradeCalendar, HammerShapeWeek, VenusShape]
# db.connect()
# db.create_tables([VenusShape])
# logger.debug('Tables created successfully.')


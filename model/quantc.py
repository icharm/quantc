# -*- coding: UTF-8 -*-

import datetime
from peewee import *
from base import config
from base import log

logger = log.Log()
db = SqliteDatabase(config.db_default)

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
    ym = CharField(unique=True)
    json = TextField()
    updated = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db


# tables = [SwStock, HammerShape, TradeCalendar]
# db.connect()
# db.create_tables([TradeCalendar])
# logger.debug('Tables created successfully.')


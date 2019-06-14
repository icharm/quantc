# -*- coding: UTF-8 -*- 
import logging
import inspect
import logging.handlers
from os.path import dirname

# 创建一个输出格式
formatter = logging.Formatter("%(levelname)s | %(asctime)s | %(name)s | %(message)s")

# 创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)


def _trackback():
    frame = inspect.currentframe().f_back.f_back
    return inspect.getframeinfo(frame)[0]

def task_log():
    name = _trackback()
    return _log(name, "task.log")

def qcinfo_log():
    name = _trackback()
    return _log(name, "qcinfo.log")

def _log(name, file):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    # 创建一个handler，用于写入日志文件, 30天分文件保存
    fh = logging.handlers.TimedRotatingFileHandler(dirname(__file__) + '/log/' + file, encoding="utf-8", when="D",
                                                   interval=30, backupCount=3)
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger

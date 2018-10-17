# -*- coding: UTF-8 -*- 
from base import config
import time

class Log:

    __postion = ''

    def __init__(self, postion):
        self.__postion = postion

    def info(self, msg):
        self.save(msg, 4)

    def error(self, msg):
        self.save(msg, 1)

    def debug(self, msg):
        self.save(msg, 3)

    def warn(self, msg):
        self.save(msg, 2)

    def save(self, msg, flag):
        log = self.spliceLogContent(msg, flag)
        if flag == 3:           # debug msg only printed in consle, don't save into log file.
            print(log)
            return
        elif config.log_out:    # print log in console, if log_out flag is True in config.
            print(log)
        try:
            f = open(config.log_path, 'a+', encoding='utf8')
            f.write(log)
            f.close()
        except Exception as e:
            print(str(e))

    def spliceLogContent(self, msg, flag):
        if flag == 1:
            log = '[x]Error|'+ self.__postion + '|' + self.getTime(1) + '|' + msg +'\n'
        elif flag == 2:
            log = '[!]Warning|'+ self.__postion + '|' + self.getTime(1) + '|' + msg + '\n'
        elif flag == 3:
            log = '[*]Debug|'+ self.__postion + '|' + self.getTime(1) + '|'+ msg + '\n'
        else:
            log = '[+]Info|'+ self.__postion + '|' + self.getTime(1) + '|'+ msg + '\n'
        return log

    #getTime according specify format
    def getTime(self, format):
        #return the time format like 2017-07-17 15:34:23
        if(format == 1):
            ISOTIMEFORMAT = '%Y-%m-%d %X'
            return time.strftime(ISOTIMEFORMAT, time.localtime())
        #return the time format like Sun Jun 15:34:23 2017
        elif(format == 2):
            return time.asctime( time.localtime(time.time()) )    
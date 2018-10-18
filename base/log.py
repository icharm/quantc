# -*- coding: UTF-8 -*- 
import time
from base import config
from base import dateutils

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
        log = self.splice_content(msg, flag)
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

    def splice_content(self, msg, flag):
        if flag == 1:
            log = '[x]Error|'+ self.__postion + '|' + dateutils.current(dateutils.DTF_FULL_NORMAL) + '|' + msg +'\n'
        elif flag == 2:
            log = '[!]Warning|'+ self.__postion + '|' + dateutils.current(dateutils.DTF_FULL_NORMAL) + '|' + msg + '\n'
        elif flag == 3:
            log = '[*]Debug|'+ self.__postion + '|' + dateutils.current(dateutils.DTF_FULL_NORMAL) + '|'+ msg + '\n'
        else:
            log = '[+]Info|'+ self.__postion + '|' + dateutils.current(dateutils.DTF_FULL_NORMAL) + '|'+ msg + '\n'
        return log 
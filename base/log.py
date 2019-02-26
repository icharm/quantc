# -*- coding: UTF-8 -*- 
import time
import inspect
from . import config

class Log:

    __postion = ''

    def __init__(self):
        traceback = self._trackback()
        self.__postion = traceback[0]

    def _trackback(self):
        frame = inspect.currentframe().f_back.f_back
        # (filename, line_number, function_name, lines, index) = inspect.getframeinfo(frame)#
        return inspect.getframeinfo(frame)

    def info(self, msg):
        self.save(msg, 4, self._trackback())

    def error(self, msg):
        self.save(msg, 1, self._trackback())

    def debug(self, msg):
        self.save(msg, 3, self._trackback())

    def warn(self, msg):
        self.save(msg, 2, self._trackback())

    def save(self, msg, flag, traceback):
        log = self.splice_content(msg, flag, traceback)
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

    def splice_content(self, msg, flag, traceback):
        log = ''
        if flag == 1:
            log += '[x]Error|'
        elif flag == 2:
            log += '[!]Warning|'
        elif flag == 3:
            log += '[*]Debug|'
        else:
            log += '[+]Info|'
        log += self.current_time() + '|' + self.__postion + '|'
        # traceback[1]: line number, traceback[2]: function name.
        log += traceback[2] + '|' + str(traceback[1]) + '|'
        log += msg + '\n'
        return log 

    def current_time(self):
        return time.strftime('%Y-%m-%d %X', time.localtime())
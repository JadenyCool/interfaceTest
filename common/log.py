# -*- coding:utf-8 -*-
import logging
import os
import datetime
import readConfig


class Log:
    def __init__(self):
        global logPath, resultPath, proDir

        self.logger = logging.getLogger("APP_interfaceTest")
        self.logger.setLevel(logging.DEBUG)

        # 判断存放路径
        # now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        curDay = datetime.date.today().__str__()
        curDir = os.path.join(readConfig.proDir, "result")
        logPath = os.path.join(curDir, curDay)

        if os.path.exists(logPath):
            logName = logPath + "//" + curDay + "_interfaceTestLog.log"
            fh = logging.FileHandler(logName, encoding="utf-8")
            fh.setLevel(logging.DEBUG)
        else:
            os.makedirs(logPath)
            logName = logPath + "//" + curDay + "_interfaceTestLog.log"
            fh = logging.FileHandler(logName, encoding="utf-8")
            fh.setLevel(logging.DEBUG)

        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(format)
        ch.setFormatter(format)

        self.logger.addHandler(fh)
        self.logger.addHandler(ch)


import threading


class MyLog:
    lock = threading.RLock()
    log = None

    def __init__(self):
        pass

    @staticmethod
    def getLog():
        if MyLog.log is None:
            MyLog.lock.acquire()
            MyLog.log = Log()
            MyLog.lock.release()
        return MyLog.log

# -*- coding:utf-8 -*-

'''
Test case module and test data update
'''
from common import configHttps
import unittest

import readUserSelfDefind as rusd
from common.log import MyLog

selfArgs = rusd.readUserDefindArgs()


def upgradeTestArgs(token, sessionId):
    '''因接口使用的Restful接口，需要注意以下几点：
        1. 登录时调用该方法
        2. 二次认证后调用该方法
    '''
    selfArgs.set_userDefindArgs("X-XSRF-TOKEN", token)
    selfArgs.set_userDefindArgs("JsessionId", sessionId)


def updateInfor(name, value):
    name1 = str(name)
    if name1.startswith('s', 0):
        selfArgs.set_PlantInfor(name, value)
    if name1.startswith('u', 0):
        selfArgs.set_UserInfor(name, value)


def getUserDefindInfor(name):
    name2 = str(name)
    if name2.startswith('s', 0):
        s = selfArgs.get_PlantInfor(name)
        return s
    if name2.startswith('u', 0):
        u = selfArgs.get_UserInfor(name)
        return u


class allCaseFunc(unittest.TestCase):

    def setUp(self):
        self.httprequest = configHttps.ConfigHttps()
        self.token = selfArgs.get_userDefindArgs("X-XSRF-TOKEN")
        self.js = selfArgs.get_userDefindArgs("JsessionId")

        self.headers = {
            "appDeviceType": "IOS",
            "language": "en_UK",
            "Content-Type": "application/json; charset=utf-8",
            "XSRF-TOKEN": self.token,
            'Cookie': "JSESSIONID=" + self.js
        }
        self.getLog = MyLog.getLog()
        self.testlog = self.getLog.logger

    def tearDown(self):
        print("--------------测试活动已结束------------------")

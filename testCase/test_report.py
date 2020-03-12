# -*- coding: utf-8 -*-
'''Report'''

from ddt import ddt, data, unpack
from common.testCaseCommon import *
import time


@ddt
class Report(allCaseFunc):

    # statDim只能是2，4，5，6  代表：日，月，年，生命周期
    # statType=1，2
    # timeZone时区
    # 增加sIds
    # 条件的结果
    @data((2, 1, 8, "", True), (2, 1, 6, selfArgs.get_PlantInfor("stationcode"), True),
          (4, 1, 5, "", True), (5, 1, -12, "", True), (6, 1, 0, "", True),
          (2, 2, -5, "", True), (2, 2, 9, "", True), (4, 3, 5, "", False), (9, 2, 4, "", False))
    @unpack
    def test_report_0001(self, value1, value2, value3, value4, value5):
        '''/rm/listKpiChart'''
        self.testlog.info("/rm/listKpiChart")
        print(value5)
        time_now = lambda: int(round(time.time() * 1000))
        print(time_now())
        url = "/rm/listKpiChart"
        data = {"statTime": "{}".format(time_now()), "statDim": "{}".format(value1), "querySource": "1",
                "statType": "{}".format(value2),
                "userId": "{}".format(selfArgs.get_UserInfor("userid")), "sIds": "{}".format(value4),
                "timeZone": "{}".format(value3)}

        self.httprequest.set_headers(self.headers)
        self.httprequest.set_data(data)
        self.httprequest.set_url(url)
        res = self.httprequest.post()
        self.testlog.info(data)
        self.testlog.info(res.text)
        self.assertEqual(value5, res.json()["success"], "Pass")

    # statDim只能是2，4，5，6  代表：日，月，年，生命周期
    # statType=1，2
    # timeZone时区
    # 增加sIds
    # 条件的结果
    @data((2, 1, 8, "", True), (2, 1, 6, selfArgs.get_PlantInfor("stationcode"), True), (4, 1, 5, "", True),
          (5, 1, -12, "", True), (6, 1, 0, "", True), (2, 2, -5, "", True), (2, 2, 9, "", True),
          (4, 3, 5, "", False), (9, 2, 4, "", False))
    @unpack
    def test_report_0002(self, value1, value2, value3, value4, value5):
        '''/rm/listKpiList'''
        url = "/rm/listKpiList"
        time_now = lambda: int(round(time.time() * 1000))
        data = {"statTime": "{}".format(time_now()), "statDim": "{}".format(value1), "statType": "{}".format(value2),
                "userId": "{}".format(selfArgs.get_UserInfor("userid")),
                "pageSize": "50", "sort": "asc",
                "orderBy": "kpiModel.fmtCollectTimeStr", "page": "1", "sIds": "{}".format(value4),
                "timeZone": "{}".format(value3)}
        self.httprequest.set_headers(self.headers)
        self.httprequest.set_data(data)
        self.httprequest.set_url(url)
        res = self.httprequest.post()
        self.testlog.info(data)
        self.testlog.info(res.text)
        self.assertEqual(value5, res.json()["success"], "Pass")

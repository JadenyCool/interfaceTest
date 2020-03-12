# -*- coding: utf-8 -*-

'''
  APP Interface Testing for Login

  author: Gu Linjie
  date : 2018-6-23
'''
from common import readWriteExcel
from common.testCaseCommon import *
import random


getLoginTestData = readWriteExcel.get_xls("testdata.xlsx",0)

class loginTest(allCaseFunc):

    # def test_user_login_01(self):
    #     '''测试登录'''
    #     data = {"loginName": "glj000", "forceLogin": "false", "password": "a1111111",
    #             "uuid": "286d59c6-a16f-44f8-94e5-49e41ecbebbb1030045537616895"}
    #     httprequest.set_headers(headers=self.headers)
    #     httprequest.set_url(getLoginTestData[0][3])
    #     httprequest.set_data(data=data)
    #     expect_result = getLoginTestData[0][-2]
    #     res = httprequest.post()
    #     test_result = res.json()["success"]
    #     dd = test_result.__str__().upper()
    #     self.assertEqual(dd, expect_result.upper(), msg="Pass")
    #     upgradeTestArgs(token=res.headers['XSRF-TOKEN'], sessionId=res.cookies['JSESSIONID'])

    def test_A_login_01(self):
        '''测试登录(/user/login)'''
        self.testlog.info("/user/login")
        Inter_URL = '/user/login'
        data ={"loginName":"glj000","forceLogin":"true","password":"a4444444","uuid":"5aaad58d-ef3e-489a-a61b-0e836ea143811030045537616895"}
        self.httprequest.set_headers(headers=self.headers)
        self.httprequest.set_url(Inter_URL)
        self.httprequest.set_data(data=data)
        res = self.httprequest.post()
        self.testlog.info(res)
        Test_result = res.json()["success"]
        self.testlog.info(Test_result)
        self.assertEqual(True, Test_result, msg="Pass")
        upgradeTestArgs(token=res.headers['XSRF-TOKEN'], sessionId=res.cookies['JSESSIONID'])
        updateInfor("userid", str(res.json()["data"]["userid"]))
        updateInfor("u_domainid", str(res.json()["data"]["domainid"]))

    # def test_A_installerRegister(self):
    #     '''安装商注册：/enroll/installerSubmit'''
    #     self.testlog.info("安装商注册：/enroll/installerSubmit")
    #
    #     playload = "abcdefghigklmnopqrstuvwxyz0123456789"
    #     random_m = random.sample(playload, 4)
    #     email_address = "".join(random_m)
    #     self.testlog.info("安装商注册新建的")
    #     url = "/enroll/installerSubmit"
    #     data = {"password":"a1111111","account":"{}@we.com".format(email_address),"surepassword":"a1111111","domianName":"{}".format(email_address),"confirmAccount":"{}@we.com".format(email_address)}
    #     #data = {"password":"a11111111","account":"gulinjie1@pinnettech.cn","surepassword":"a11111111","domianName":"dsf","confirmAccount":"gulinjie1@pinnettech.cn"}
    #     self.httprequest.set_headers(headers=self.headers)
    #     self.httprequest.set_url(url)
    #     self.httprequest.set_data(data
    # =data)
    #     res = self.httprequest.post()
    #     self.testlog.info(res.text)
    #     Test_result = res.json()["success"]
    #     self.testlog.info(Test_result)
    #     self.assertEqual(True, Test_result, msg="Pass")

    def test_P_Lat_Longit_001(self):
        '''上报经纬度/app/position'''
        self.testlog.info("上报经纬度/app/position")
        url = "/app/position"
        data = {"latitude": "31.247196038642187", "longitude": "121.49237750590044"}
        self.httprequest.set_headers(headers=self.headers)
        self.httprequest.set_url(url)
        self.httprequest.set_data(data=data)
        res = self.httprequest.post()
        self.testlog.info(res.text)
        self.assertEqual(True, res.json()['success'], res.text)








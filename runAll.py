# -*- coding : utf-8 -*-
import unittest
from common import HTMLTestReportCN
import os, time
import readConfig
from common import configEmail
import datetime

from common.log import MyLog

getlog = MyLog.getLog()
Out_log = getlog.logger


def Suite():
    suiteTest = unittest.TestSuite()
    testfiles = []
    caseFailePath = os.path.join(readConfig.proDir, "testCase")
    discover = unittest.defaultTestLoader.discover(caseFailePath, pattern="test_*.py", top_level_dir=None)
    testfiles.append(discover)
    if testfiles:
        for test_file in testfiles:
            suiteTest.addTests(test_file)
    else:
        Out_log.info("No case can be run!!!!")
        return False
    return suiteTest


def run():
    all_test_case = Suite()
    curDay = datetime.date.today().__str__()
    # day = time.strftime("%Y-%m-%d",time.localtime(time.time()))
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    tdresult = ".\\result\\" + curDay

    try:
        if all_test_case:
            if os.path.exists(tdresult):
                filename = tdresult + "\\" + now + "_report.html"
                fp = open(filename, "wb")
                runner = HTMLTestReportCN.HTMLTestRunner(
                    stream=fp,
                    title=u'APP-interfaceTest(SPC600) 自动化测试报告',
                    description='1. 当前测试接口来源SPC600; '
                                '2. 测试接口只涉及：（1）注册户用账号以及更新用户信息；（2）新建电站以及更新电站信息；'
                                '                （3）“我的”整个模块的接口; (4)安装商注册。'
                                '3. 测试服务器版本：SPC700',  # 不传默认为空
                    tester=u"Jerry"  # 测试人员名字，不传默认为QA
                )
                runner.run(all_test_case)
            else:
                os.makedirs(tdresult)
                filename = tdresult + "\\" + now + "_report.html"
                Out_log.info("Create path: {}".format(filename))
                fp = open(filename, "wb")
                runner = HTMLTestReportCN.HTMLTestRunner(
                    stream=fp,
                    title='SPC600接口自动化测试报告',
                    description='SPC600接口详细测试用例结果',  # 不传默认为空
                    tester="Jerry Gu"  # 测试人员名字，不传默认为QA
                )
                runner.run(all_test_case)
        else:
            Out_log.info("No case can be run!!!!")
    except Exception as e:
        Out_log.error(e)
    return filename


if __name__ == "__main__":
    Out_log.info("The Interface Test is starting.....")
    getGerareport = run()
    try:
        if os.path.exists(getGerareport):
            configEmail.conEmail().sendMail(getGerareport)
        else:
            print("Not send success!!!")
    except FileNotFoundError as e:
        Out_log.error("Report File is not exit")
        Out_log.error(e)

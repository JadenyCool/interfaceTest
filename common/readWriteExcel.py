# -*- coding:utf-8 -*-
import os
from xlrd import open_workbook
from common.log import MyLog
import readConfig
import xlsxwriter

getlog = MyLog.getLog()
log = getlog.logger

localReadConfig = readConfig.ReadConfig()


def get_xls(xls_name, sheet_index):
    cls = []
    xlsPath = os.path.join(readConfig.proDir, "testFile", xls_name)

    if os.path.exists(xlsPath):
        log.info(xlsPath + ' ' + "测试数据获取正常")

    else:
        log.error('No test Data exist!!!!')
        print('''解决方式如下:
                       1.检查testFile中是否放置了测试数据文件；
                       2.检查config.ini配置文件中是否将testdata路径设置正确''')

    file = open_workbook(xlsPath)
    # sheet = file.sheet_by_name(sheet_name)
    sheet = file.sheet_by_index(sheet_index)
    nrows = sheet.nrows
    for i in range(1, nrows):
        if sheet.row_values(i)[1] != "caseName":
            cls.append(sheet.row_values(i))
    return cls

# def write_xls(xls_name,sheet_index):
#     pass
#     xls_path = os.path.join(readConfig.proDir,"testFile",xls_name)
#     # file = open_workbook(xls_path)
#     # sheet = file.sheet_by_index(sheet_index)
#     # nrows = sheet.nrows
#
#     workbook = xlsxwriter.Workbook(xls_path)
#

# if __name__ == "__main__":
# #     a=get_xls("testdata.xlsx",0)
# #     print(a)
# b = write_xls("testdata.xlsx","LoginAndFirstPagetestData")

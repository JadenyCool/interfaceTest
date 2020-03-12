# -*- coding:utf-8 -*-

import readConfig
from common.log import MyLog
import pymysql as sqldb

localReadConfig = readConfig.ReadConfig()


class configDB:
    def __init__(self):
        global host, port, username, password, database
        host = localReadConfig.get_db("host")
        port = localReadConfig.get_db("port")
        username = localReadConfig.get_db("username")
        password = localReadConfig.get_db("password")
        database = localReadConfig.get_db("database")
        # init log class
        self.getLog = MyLog.getLog()
        self.log = self.getLog.logger

    def connection(self, sqlstatus):
        try:
            connection = sqldb.connect(host=host, port=port, user=username, password=password, db=database,
                                       charset='utf8mb4', cursorclass=sqldb.cursors.DictCursor)
            self.log.info("Database has been connected successfully")
        except Exception as e:
            self.log.error("Database connect fail !!!")
            self.log.error(e)
        try:
            curs = connection.cursor()
            curs.execute(sqlstatus)
            self.log.info("execute sql : {}".format(sqlstatus))
            result = curs.fetchone()
            connection.close()
            return result
        except Exception as e1:
            self.log.error(e1)
            self.log.error("sql check error !!!, please check sql statement")

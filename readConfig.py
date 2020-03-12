# -*- coding:utf-8 -*-
import configparser
import os

proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir, "config.ini")


class ReadConfig():
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(configPath, encoding="utf-8")

    def get_db(self, name):
        value = self.cf.get("DATABASE", name)
        return value

    def get_https(self, name):
        value = self.cf.get("HTTPS", name)
        return value

    def get_email(self, name):
        value = self.cf.get("EMAIL", name)
        return value

    # def get_userDefinedArgs(self,name):
    #     value = self.cf.get("USERDEFINEDARGS",name)
    #     return value
    #
    # def set_userDefinedArgs(self,name,value):
    #     self.cf.set("USERDEFINEDARGS", name, value)
    #     fp = open(configPath,'w')
    #     self.cf.write(fp)

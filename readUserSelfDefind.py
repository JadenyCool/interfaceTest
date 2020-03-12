# -*- encoding: utf-8 -*-
'''
  User self-defind args file, such as : token, jsessionId, username, password ect.
'''

import os
import configparser

self_proDir = os.path.split(os.path.realpath(__file__))[0]
filePath = os.path.join(self_proDir, "user-defindArgs.ini")


class readUserDefindArgs:

    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(filePath, encoding="utf-8")

    def get_userDefindArgs(self, name):
        value = self.cf.get("UDEFINDARGS", name)
        return value

    def set_userDefindArgs(self, name, value):
        self.cf.set("UDEFINDARGS", name, value)
        fp = open(filePath, "w")
        self.cf.write(fp)

    def get_PlantInfor(self, name):
        value = self.cf.get("PLANTINFOR", name)
        return value

    def set_PlantInfor(self, name, value):
        self.cf.set("PLANTINFOR", name, value)
        fp = open(filePath, 'w')
        self.cf.write(fp)

    def get_UserInfor(self, name):
        value = self.cf.get("USERINFOR", name)
        return value

    def set_UserInfor(self, name, value):
        self.cf.set("USERINFOR", name, value)
        fp = open(filePath, 'w')
        self.cf.write(fp)

# -*- coding:utf-8 -*-
import requests
import readConfig
from common.log import MyLog

requests.packages.urllib3.disable_warnings()

localReadConfig = readConfig.ReadConfig()


class ConfigHttps:
    def __init__(self):
        global host, port, timeout
        host = localReadConfig.get_https("baseurl")
        port = localReadConfig.get_https("port")
        timeout = localReadConfig.get_https("timeout")
        self.getLog = MyLog.getLog()
        self.log = self.getLog.logger
        self.headers = {}
        self.params = {}
        self.data = {}
        self.url = None
        self.files = {}

    def set_url(self, url):
        self.url = host + url

    def set_headers(self, headers):
        self.headers = headers

    def set_params(self, params):
        self.params = params

    def set_data(self, data):
        self.data = data

    def set_files(self, files):
        self.files = files

    def post(self):
        try:
            if self.files:
                response = requests.post(self.url, json=self.data, headers=self.headers, files=self.files,
                                         timeout=float(timeout), verify=False)
                return response
            else:
                response = requests.post(self.url, json=self.data, headers=self.headers, timeout=float(timeout),
                                         verify=False)
                return response
        except TimeoutError:
            self.log.error("Request Time Out!")
            return None

    def get(self):
        try:
            response = requests.get(self.url, params=self.params, headers=self.headers, timeout=float(timeout),
                                    verify=False)
            return response
        except TimeoutError:
            self.log.error("Request Time Out!")
            return None

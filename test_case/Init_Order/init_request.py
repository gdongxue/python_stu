# -*- coding:utf-8 -*-
import requests
from test_case import Login
def initorder(self):

        self.data = {
    }
        self.io = requests.get(url=self.url, params=self.data, cookies=self.cookies)
        return self.io
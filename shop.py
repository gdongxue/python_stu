# -*- coding:utf-8 -*-
import requests
import Login
import unittest
import json

class Shop(unittest.TestCase):

    def setUp(self):
        self.url = "http://api.100iec.com/shop/getinfo"
        self.login = Login.login()
        self.cookie = self.login.cookies
    def test_shopid (self):
        open= json.loads(self.login.text)
        print open
        o = open["result"]["openid"]
        print "userid is:" + o
        data ={
            "shopid":o
        }
        self.url = self.url + "?shopid="+o
        shopinfo  = requests.get(self.url,cookies = self.cookie)
        print shopinfo.text
    def tearDown(self):
        pass
if __name__ == '__main__':
    unittest.main
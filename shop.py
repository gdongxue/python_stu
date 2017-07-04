# -*- coding:utf-8 -*-
import requests
import Login
import unittest

class Shop(unittest.TestCase):

    def setUp(self):
        self.url = "http://api.100iec.com/shop/getid"
        self.cookie = Login.login()
    def test_shopid (self):
        m = requests.get(self.url,cookies = self.cookie)
        print m.text
    def tearDown(self):
        pass
if __name__ == '__main__':
    unittest.main
# -*- coding:utf-8 -*-
import requests
import Login
import unittest
import json

class Shop(unittest.TestCase):
    # 获取店铺信息
    def setUp(self):
        self.url = "http://api.100iec.com/shop/getinfo"
        self.url1 = "http://api.100iec.com/shop/getShopGoods"
        self.login = Login.login()
        self.cookie = self.login.cookies

    def test_shopinfo (self):
        open = json.loads(self.login.text)
        # 将字符串转化字典
        o = open["result"]["openid"]
        print "userid is:" + o
        self.url = self.url + "?shopid="+o
        shopinfo  = requests.get(self.url,cookies = self.cookie)
        print shopinfo.text

#     获取店铺商品
    def test_shop_goods(self):
        openid = json.loads(self.login.text)
        shopid = openid["result"]["openid"]
        self.url_goods = self.url1+"?shopid"+shopid
        goods = requests.get(url=self.url1,cookies = self.cookie)
        print goods.text

    def tearDown(self):
        pass
if __name__ == '__main__':
    suit = unittest.TestSuite
    suit.addTest(Shop("test_shopinfo"))
    suit.addTest(Shop("test_shop_goods"))
    runner = unittest.TextTestRunner
    runner.run(suit)
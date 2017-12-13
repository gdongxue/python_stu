# -*- coding:utf-8 -*-
import requests
from test_case import Login
import unittest
import json
class Cart:
    def setUp(self):
        self.login = Login.login()
        self.cookies = self.login.cookies
        # 获取购物车数量
        self.getcartcount_url = "http://api.100iec.com/cart/getcartcount"
        # 添加购物车
        self.add_url = "http://api.100iec.com/cart/addCart"
        # 初始化购物车
        self.getinfo_url = "http://api.100iec.com/cart/getcartinfo"
    # 添加购物车
    def add_cart(self):
        data = {
            "goodsId":"73",
            "number":"2",
            "selleropenId":"U170802117982617126"
        }
        cart = requests.get(url=self.add_url,params=data,cookies = self.cookies)
        # print cart.text
    #  获取购物车数量
    def getcount(self):
        getcount = requests.get(url=self.getcartcount_url,cookies = self.cookies)
        print getcount.text

    # 初始化购物车列表
    def getinfo(self):
        data ={
            "openId":"U170802117982617126"
        }
        getinfo = requests.get(url= self.getinfo_url,params=data,cookies = self.cookies)
        # print getinfo.text
        # 将字符串转化为字典
        cartid = json.loads(getinfo.text)
        # 获取字典的中的元素，得到的为列表
        cartlist = cartid["result"]["list"]
        for i in  cartlist:
            # print i
            self.cartl = i["cartid"]
            print self.cartl
            return self.cartl

if __name__ == '__main__':
   unittest.main()
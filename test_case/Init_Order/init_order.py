# -*- coding:utf-8 -*-
import unittest
import requests
from test_case import Login
import ConfigParser
import config
import init_request
import json
from  test_case.Cart.AddCart import Cart

class Order(unittest.TestCase,Cart):
    def setUp(self):
        self.url = "http://api.100iec.com/order/initOrder"
        self.login = Login.login()
        self.cookies = self.login.cookies
#公共方法 获取运费值
    def comm_request(self,data):
        a = requests.get(url=self.url,params=data,cookies = self.cookies)
        expressFee = json.loads(a.text)
        expressFee = expressFee["result"]["price"]
        expressFee = expressFee["expressFee"]
        expressFee = expressFee.encode("utf-8")
        return expressFee

# 只购买供应商商品，商品数量为1，地点为北京，运费=0
    def test_case1(self):
        data ={
            "orderType":1,
            "goodsId":"58",
            "addressId":"1751"
        }
        expressFee = self.comm_request(data)
        self.assertEqual(expressFee, "0.00")
        print "只购买供应商商品，商品数量为1，地点为北京，运费=0"

# 只购买常温自营商品，商品数量为1，地点为可配送范围之内(长春)，首重为2,（3.5+6.5=10）
    def test_case2(self):
        data = {
            "orderType": 1,
            "goodsId": "61",
            "addressId": "2047"
        }
        expressFee = self.comm_request(data)
        self.assertEqual(expressFee,"10.00")
        print "只购买常温自营商品，商品数量为1，地点为可配送范围之内(北京),运费=10"

# 达到包邮门槛，购买>99元的自营商品，运费=0 ，下单地址在可配送范围之内（山西）
    def test_case3(self):
      cart = self.getinfo()
      # print self.cart
      # data = {
      #      "orderType": 1,
      #      "cartIdList": self.cart,
      #      "addressId": "1751"
      # }
      # expressFee = self.comm_request(data)
      # print expressFee

    def tearDown(self):
        pass
if __name__ == '__main__':
    unittest.main
# -*- coding:utf-8 -*-
import requests
import unittest
import Login
import json

class CreateOrder(unittest.TestCase):
    def setUp(self):
        self.curl = "http://api.100iec.com/order/createOrder"
        self.ourl = "http://api.100iec.com/order/orderinfo"
        self.login = Login.login()
        self.cookie = self.login.cookies
    def create(self):
         data = {
                    "dispatchtype": 0,
                    "addressid": 1420,
                    "fromcart": 2,
                    "goods": "47,0,1",
                    "carrier": 1,
                }
         order = requests.post(self.curl, data=data,cookies = self.cookie)
         # 将字符串转换为字典
         res = json.loads(order.text)
         # 获取ordersn
         ordersn = res["result"]["ordersn"]
         print ordersn
         return ordersn

    def test_order_message(self):
        ordersn = self.create()
        data = {
            "ordersn":ordersn
        }
        om = requests.get(url=self.ourl,params=data)
        print om.text
    def tearDown(self):
        pass
if __name__ == '__main__':
    suit = unittest.TestSuite
    suit.addTest(CreateOrder("test_order_message"))
    runner = unittest.TextTestRunner
    runner.run(suit)



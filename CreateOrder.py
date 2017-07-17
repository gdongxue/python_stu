# -*- coding:utf-8 -*-
import requests
import unittest
import Login
import json
import HTMLTestRunner
import Adress

class CreateOrder(unittest.TestCase):
    def setUp(self):
        # 创建订单
        self.curl = "http://api.100iec.com/order/createOrder"
        # 订单详情
        self.ourl = "http://api.100iec.com/order/orderinfo"
        self.login = Login.login()
        self.cookie = self.login.cookies
    def create(self):
        data = {
            "dispatchtype": 0,
            "addressid": 1635,
            "fromcart": 2,
            "goods": "47,0,1",
            "carrier": 1,
            "deduct2":1
        }
        order = requests.post(self.curl, data=data, cookies=self.cookie)
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
        message = json.loads(om.text)
        result = message["result"]
        print result
        flag = 0
        for i in  result:
            if (i == "U170711166074675802"):
                print "下单人正确"
                break
            else:
                print "下单人不正确"

        if(flag==0):
                print "下单人正确"
    def tearDown(self):
        pass
if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(CreateOrder("test_order_message"))
    Htmlfile = "E:\\test\\OrderResult.html"
    fp = open(Htmlfile,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title="测试报告",
        description="用例执行情况"
    )
    runner.run(suit)
    fp.close()



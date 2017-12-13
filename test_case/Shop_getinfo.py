# -*- coding:utf-8 -*-
import unittest
import requests
import Login
import json
import ConfigParser
import HTMLTestRunner

class ShopInfo(unittest.TestCase):
    def setUp(self):
        self.url = "http://api.100iec.com/shop/getinfo"
    def test_shop_getinfo(self):
        # 读取配置文件
        cf = ConfigParser.ConfigParser()
        cf.read("test.ini")
        cd_status = cf.get("code","status")
        cd_status1 = int(cd_status)

        data = {
            "shopid":"U170616112232354653"
        }
        self.cookie = Login.login()
        shopinfo = requests.get(self.url,data,cookies = self.cookie)
        res = shopinfo.json()

        self.assertEqual(res["status"],cd_status1)

        self.assertEqual(shopinfo.status_code, 200)
        print shopinfo.text

    def tearDown(self):
        pass
if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(ShopInfo("test_shop_getinfo"))
    HTmlfile = "E:\\test\\result.html"
    fp = file(HTmlfile,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title="测试报告",
        description="用例执行情况"
    )
    runner.run(suit)
    fp.close()
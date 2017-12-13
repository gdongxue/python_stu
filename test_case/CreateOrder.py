# -*- coding:utf-8 -*-
import unittest
import requests
import Login
import ConfigParser
import json
import config
# todo
class CreateOrder (unittest.TestCase):
    def setUp(self):
        # 获取商品详情
        self.detailUrl = "http://api.100iec.com/goods/getGoodsDetail"
        self.login = Login.login()
        self.cookie=self.login.cookies
    def test_goodsDetail(self):
        cf = ConfigParser.ConfigParser()
        cf.read("test.ini")
        name = cf.get("code","title")
        # namede = name.decode('utf-8')
        print name
        data = {
            "goodsId":"52"
        }
        goodsDetail = requests.get(url=self.detailUrl,params=data,cookies=self.cookie)
        goodName = json.loads(goodsDetail.text)
        tit = goodName["result"]["goods"]
        title = tit["title"]
        titl = title.encode("utf-8")
        self.assertEqual(name,titl)
        print titl

    def tearDown(self):
        pass
if __name__ == '__main__':
    unittest.main
# -*- coding:utf-8 -*-
import requests
import Login
import unittest
import json

class Shop(unittest.TestCase):

    def setUp(self):
        # 获取店铺信息
        self.url = "http://api.100iec.com/shop/getinfo"
        # 获取当前店铺商品列表
        self.url1 = "http://api.100iec.com/shop/getShopGoods"
        # 获取商品上下架接口
        self.url2 = "http://api.100iec.com/shop/setshopgoods"
        self.login = Login.login()
        self.cookie = self.login.cookies

    # 获取店铺信息
    def shopinfo (self):
        open = json.loads(self.login.text)
        # 将字符串转化字典
        o = open["result"]["openid"]
        self.url = self.url + "?shopid="+o
        shopinfo  = requests.get(self.url,cookies = self.cookie)
        # print shopinfo.text

    # 获取店铺商品
    def shop_goods(self):
        openid = json.loads(self.login.text)
        shopid = openid["result"]["openid"]
        self.url_goods = self.url1+"?shopid="+shopid
        goods = requests.get(url=self.url_goods,cookies = self.cookie)
        print goods.text
        return goods.text

    # 获取店铺商品上下架状态
    def test_setshop_goods(self):
        # 调用获取店铺商品状态方法
        goodsStatus = self.shop_goods()
        # 将字符串转化为字典
        goodsta = json.loads(goodsStatus)
        goodstatusList = goodsta["result"]["goods"]
        flag = 0
        for obj in goodstatusList:
            if (obj["id"] == "52"):
                 data = {
                        "goodsId":52,
                        "type":"down"
                    }
                 set_shop = requests.get(url=self.url2,params=data,cookies = self.cookie)
                 print set_shop.text
                 flag = 1
                 break
            else:
                pass
        if(flag == 0):
            data = {
                "goodsId": 52,
                "type": "up"
            }
            set_shop = requests.get(url=self.url2, params=data, cookies=self.cookie)
            print set_shop.text
    def tearDown(self):
        pass
if __name__ == '__main__':
    unittest.main
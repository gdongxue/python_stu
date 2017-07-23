# -*- coding:utf-8 -*-
import requests
import json
import Login
import unittest
class Adress(unittest.TestCase):
    def setUp(self):
        # 获取当前登录用户全部地址
        self.allUrl = "http://api.100iec.com/member/address/getall"
        # 新增收货地址
        self.addUrl = "http://api.100iec.com/member/address/update"
        # 删除收货地址
        self.deUrl = "http://api.100iec.com/member/address/delete"
        # 获取登录信息
        self.login = Login.login()
        self.cookie = self.login.cookies

    def add_adress(self):
        data = {
            "id":0,
            "realname":"高冬雪",
            "mobile":"13611111111",
            "province":"220000",
            "city":"220100",
            "area":"220112",
            "address":"圣朝菲6号楼3层301",
            "isdefault":1
        }
        addAdress = requests.get(url=self.addUrl,params=data,cookies = self.cookie)
        print addAdress.text
        return addAdress

    def test_de_adress(self):
        address = self.add_adress()
        addresst = json.loads(address.text)
        id = addresst["result"]["lastInsertId"]
        data = {
            "id":id
        }
        deAdress = requests.get(url= self.deUrl,params=data,cookies = self.cookie)
        print deAdress.text

    def test_all_adress(self):
        allAdress = requests.get(url=self.allUrl, cookies=self.cookie)
        print allAdress.text

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main

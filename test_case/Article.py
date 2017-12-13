# -*- coding:utf-8 -*-
import unittest
import requests
class Article(unittest.TestCase):
    def setUp(self):
        # 新手入门&课程精选列表
        self.list_url = "http://api.100iec.com/article/article/getlist"
        # 课程详情
        self.detail_url= "http://api.100iec.com/article/article/detail"
        #
    def test_list(self):
        list = requests.get(self.list_url)
        print list.text
    def test_detail(self):
        data = {
            "id" :25
        }
        detail = requests.get(self.detail_url,params=data)
        print detail.text
    def tearDown(self):
        pass
if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(Article("test_list"))
    suit.addTest(Article("test_detail"))
    runner = unittest.TextTestRunner()
    runner.run(suit)
    # unittest.main
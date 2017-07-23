# -*- coding:utf-8 -*-
import unittest
import CreateOrder
import Adress
import  Shop
import Goods
import HTMLTestRunner
import sys

reload(sys)
sys.setdefaultencoding('utf8')
class RunAll(unittest.TestCase):

    def setup(self):

        pass
    def tearDown(self):
        pass
if __name__ == '__main__':
    # 添加测试组件
    suit = unittest.TestSuite()
    suit.addTest(unittest.makeSuite(CreateOrder.CreateOrder))
    suit.addTest(unittest.makeSuite(Adress.Adress))
    suit.addTest(unittest.makeSuite(Shop.Shop))
    suit.addTest(unittest.makeSuite(Goods.Good))
    filename = "E:\\test\\result1.html"
    fp = open(filename,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(
        stream = fp,
        title = "自动化报告",
        description ="详细描述如下："

    )
    # runner = unittest.TextTestRunner()
    runner.run(suit)
    fp.close()

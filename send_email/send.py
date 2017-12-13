# -*- coding:utf-8 -*-
from selenium import webdriver
import web_selenium
import time
import unittest
from HTMLTestRunner import HTMLTestRunner

from selenium.webdriver.common.action_chains import ActionChains
class Send(unittest.TestCase):
    """
    qq邮件发送报告
    """
    def setUp(self):
        driver = webdriver.Chrome()
        web_selenium.Login().login(driver)
        self.driver=driver
    def test_send(self):
        """
        搜索测试用例

        """
        self.driver.find_element_by_xpath("//*[@id='composebtn']").click()
        #添加收件人
        self.driver.switch_to_frame("mainFrame")
        e1= self.driver.find_element_by_xpath('//*[@id="toAreaCtrl"]')
        action= ActionChains(self.driver)
        time.sleep(2)
        action.move_to_element(e1).click().send_keys("714131254@qq.com").perform()

        #书写主题
        time.sleep(2)
        e2=self.driver.find_element_by_xpath('//*[@id="subject"]')
        action=ActionChains(self.driver)
        action.move_to_element(e2).click().send_keys(u"测试邮件").perform()

        #书写正文
        time.sleep(2)
        e3=self.driver.find_element_by_xpath('/html/body')
        action=ActionChains(self.driver)
        action.move_to_element(e3).click().send_keys(u"你就是个大傻瓜❤！").perform()

        #点击发送按钮
        self.driver.find_element_by_xpath('//*[@id="toolbar"]/div/a[1]').click()
        def tearDown(self):
            self.driver.quit()
if __name__ == '__main__':
    testunit= unittest.TestSuite()
    testunit.addTest(Send("test_send"))
    time=time.strftime("%y-%m-%d")
    test_report="C:\\Users\\dongxue\\PycharmProjects\\test\\send_email\\"+time+" result.html"
    fp=open(test_report,"wb")
    runner=HTMLTestRunner(
        stream=fp,
        title=u"qq发送邮件测试报告",
        description=u"用例执行情况"
    )
    runner.run(testunit)
    fp.close()
    # dri=Send()
    # dri.send(driver)
    # unittest.main()
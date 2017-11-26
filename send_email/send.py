# -*- coding:utf-8 -*-
from selenium import webdriver
import web_selenium
import time
from selenium.webdriver.common.action_chains import ActionChains
class Send():
    def send(self,driver):
        web_selenium.Login().login(driver)
        driver.find_element_by_xpath("//*[@id='composebtn']").click()
        #添加收件人
        driver.switch_to_frame("mainFrame")
        e1= driver.find_element_by_xpath('//*[@id="toAreaCtrl"]')
        action= ActionChains(driver)
        action.move_to_element(e1).click().send_keys("714131254@qq.com").perform()

        #书写主题
        e2=driver.find_element_by_xpath('//*[@id="subject"]')
        action=ActionChains(driver)
        action.move_to_element(e2).click().send_keys(u"测试邮件").perform()

        #书写正文
        e3=driver.find_element_by_xpath('/html/body')
        action=ActionChains(driver)
        action.move_to_element(e3).click().send_keys(u"你就是个大傻瓜❤！").perform()

        #点击发送按钮
        driver.find_element_by_xpath('//*[@id="toolbar"]/div/a[1]').click()
if __name__ == '__main__':
    driver=webdriver.Chrome()
    dri=Send()
    dri.send(driver)
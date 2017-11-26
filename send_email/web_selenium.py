# -*- coding:utf-8 -*-
from selenium import webdriver
import time
import selenium.webdriver.support.ui as ui
class Login():
    def login(self,driver):
        driver.get("https://mail.qq.com/")
        driver.maximize_window()
        driver.switch_to_frame("login_frame")
        driver.find_element_by_id("switcher_plogin").click()
        driver.find_element_by_xpath("//*[@id='u']").send_keys("1564260446")
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='p']").send_keys("xue123456")
        driver.find_element_by_id("login_button").click()
        time.sleep(3)



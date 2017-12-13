# -*- coding:utf-8 -*-
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://baidu.com")
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/span[1]/input").send_keys(u"高冬雪")
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div").click()
driver.quit()


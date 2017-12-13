# -*- coding:utf-8 -*-
import requests
import unittest
def login():
    url = "http://100iec.com/test/memberlogin"
    data = {
        "openid":"U170802117982617126"
    }
    login =requests.get(url=url,params=data)
    print login.text

if __name__ == '__main__':
 login()

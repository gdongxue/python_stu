# -*- coding:utf-8 -*-
import requests
def login():
    url = "http://api.100iec.com/member/login/mobile"
    login_data = {
            "mobile": "17800000000",
            "code": "123456"
        }
    login = requests.get(url,login_data)
    print login.text
    cookie = login.cookies
    return cookie


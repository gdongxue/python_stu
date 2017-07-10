# -*- coding:utf-8 -*-
import requests
import json
def login():

    # 发送验证码
    url2 = "http://api.100iec.com/util/sms/logincode/send"
    code_data = {
        "mobile":"17800000000",
        "code":"rh7n"
    }
    code = requests.get(url2,params=code_data)
    cookie = code.cookies

    # 登录
    code_text = json.loads(code.text)
    code = code_text["result"]["code"]


    url = "http://api.100iec.com/member/login/mobile"
    login_data = {
            "mobile": "17800000000",
            "code": code
        }
    login = requests.get(url,params=login_data,cookies = cookie)
    # print login.text
    # cookie = login.cookies
    return login

if __name__ == '__main__':
 login()

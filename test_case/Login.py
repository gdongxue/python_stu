# -*- coding:utf-8 -*-
import requests
import json
def login():

    # 发送验证码
    url2 = "http://api.100iec.com/util/sms/logincode/send"
    code_data = {
       "mobile":"18077777777",
        "code":"rh7n"
     }
    code = requests.get(url2,params=code_data)
    cookie = code.cookies

    # 登录
    code_text = json.loads(code.text)
    code = code_text["result"]["code"]

    url = "http://api.100iec.com/member/login"
    login_data = {
            "action":"mobileLogin",
            "mobile": "18077777777",
            "code": code
        }
    header = {
        "Appinfo":"123456"
    }
    login = requests.get(url=url,params=login_data,headers=header,cookies=cookie)
    return login

if __name__ == '__main__':
 login()

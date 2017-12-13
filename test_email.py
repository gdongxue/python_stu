# -- coding:utf-8 --
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr
from send_email.send import Send
import unittest
import time
from HTMLTestRunner import HTMLTestRunner
import os


def format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
# 发送人
sender = "1564260446@qq.com"
# 接收人
receiver = "714131254@qq.com"
# 主题
subject = "python email test"
username = "1564260446@qq.com"
# 密码需要配置为qq邮箱的password
password = "taoswgayqxaljjfd"
# 发送内容
msg = MIMEText(test_report, "plain", "utf-8")
msg["Subject"] = Header(subject, "utf-8")
msg["From"] = format_addr('冬雪 <%s>' % sender)
msg["To"] = format_addr('立志 <%s>' % receiver)
# qq服务器个端口号网上有
smtp = smtplib.SMTP_SSL("smtp.qq.com", 465)

# 链接qq服务器
smtp.connect("smtp.qq.com")
# qq邮箱登录
smtp.login(user=username, password=password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
print "Email has been sent out"



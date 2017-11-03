# -*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
# 发送邮件
sender = "1564260446@qq.com"
# 接收文件
receiver = "714131254@qq.com"

subject="python email test"
username ="1564260446@qq.com"
password ="taoswgayqxaljjfd"
msg =MIMEText("你好WDewfrefrgtytgtb","text","utf-8")
msg["Subject"]=Header(subject,"utf-8")

msg['From'] = sender('Python爱好者 <%s>' % sender)
msg['To'] = receiver('管理员 <%s>' % receiver)

smtp=smtplib.SMTP_SSL("smtp.qq.com", 465)
smtp.connect("smtp.qq.com")
smtp.login(user=username,password=password)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()
print "Email has been sent out"

# -*- coding:utf-8 -*-
import yagmail
yag = yagmail.SMTP(user="1564260446@qq.com",password="jbjvvuhiqfjmhjea",host="smtp.qq.com")
contents=[u"立志,你就是个大傻子！哈哈哈哈....."]
yag.send("zglizhi@126.com",u"我发的邮件",contents=contents,)
print u"邮件发送成功"
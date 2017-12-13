# -*- coding:utf-8 -*-
a = "gaodongxue"
print a.capitalize()
# print a.center(20,fillchar="j")
print a.upper()
print a.lower()
print a.swapcase()
b = "123"
print b.isdigit()
print a.isalpha()
print b.isalnum()
print a.isspace()
c="Gaod"
d = " g d"
print c.islower()
print d.isspace()
e = " "
print e.isspace()
print abs(-123)
str="高东雪"
print str.decode(encoding="utf-8")
print type(u"高东雪")
print type("高东雪")
sum = 0
for i in range(0,101):
    if (i<101):
        sum  =sum+i
print sum
str="上海交大"
a={
    "name":"gaodongxue",
    "age":20,
    "school":str
}
print a["name"]
print a.keys()

print a.values()

print a.items()
print str

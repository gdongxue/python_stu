 # -*- coding:utf-8 -*-
from collections import Iterator
from collections import Iterable
# str = u"gao"
# print str
# a = str.encode("utf-8")
# print type(a)
# print a
# b= "hello %s,My name is %s"%("高冬雪","张立志")
# print b
# c = {"gaodongxue":27,"zhanglizhi":29}
# c["jack"]=20
# print c
# "gaodongxue" in c
# d= c.get("gaodongxue")
# print d
# for key in c:
#     print key
# for key in c:
#     print key,":",c[key]
# s = set([1,2,3])
# print s
# s.add(7)
# print s
#
# d1 ={"dog":3,"cat":4,"pig":5}
# d2 ={"eleplant":3,"moeky":9}
# d = dict(d1.items()+d2.items())
# print d
# d3 = dict(d1,**d2)
# print d3
# d4=dict(d1)
# d4.update(d2)
# print d4
# s =set([("Adam",23),("Lisa",32),("Bart",29)])
# for x in s:
#  print x[0],":",x[1]
#
# f=("gaodongxue")
# f1 =sorted(f)
# print f1
#
# j = [1,24,342,24,35,213,214,2]
# j1 = sorted(j)
# print j1
# # j2 = j.sort()
# # print j2
#
# d5 ={"dog":9,"cat":4,"pig":5}
# d8 = sorted(d5.keys())
# print d8
# d7 = sorted(d5.values())
# print d7
# d6 = sorted(d5)
# print d6
#
# o = cmp(2,9)
# print o
#
# p = abs(-100)
# print p
#
# s =set([("Adam",23),("Lisa",32),("Bart",29)])
# for x in s:
#  print x[0],":",x[1]
# def index(r):
#     print r
# index("这是一个方法")
# def add(a,b):
#     print a+b
# X=add(4,9)
# print X
# def add_1():
#     s =0
#     for i in range(0,3):
#          s =s+i
#          print s
# add_1()
# def power(x,n=2):
#     s=1
#     while n>0:
#         n=n-1
#         s=s*x
#         print s
# power(3)
# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     print sum
# calc(1,2)
# def persion(name,age,**kwargs):
#     print "name:",name,"age",age,"other:",kwargs
# persion("gaodongxue0",29,city="beijing")

def presion_1(name,age,*,city="beijing",job):
    print(name,age,city,job)
presion_1("gaodongxe",20,job="worker")
presion_1("zhanglizhi",90,city="shanghai",job="it")
L = list(range(0,101))
print(L)
print(L[0::5])
t=(1,2,3,4,5)
print(t[0:3])
str="gaodongxue"
print(str[0:3])
print(isinstance(iter(str),Iterator))
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
odd()


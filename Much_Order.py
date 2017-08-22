# -*- coding:utf-8 -*-
# 自动下单 同一用户连续下三单
from CreateOrder import *
def much_order():
    i = 0
    for i in  range(10):
        if i<=3:
            order = CreateOrder()
            a = order.create()
            print a
            i=i+1
        else:
            break
# if __name__ == '__main__':
much_order()

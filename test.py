# -*- coding:utf-8 -*-

print type(list(map(str,[1,2,3,4])))


def add (x,y,f):
    return f(x)+f(y)
print add(5,-6,abs)


L=[-1,2,3,4,5,6,-1,0,100]
print map(abs,L)

def f(x,y):
    return x+y
print reduce(f,L)

def is_odd(x):
    return x%2==0
print filter(is_odd,L)

def f(n):
    return str(n)[0:2]==str(n)[::-2]
print filter(f,[12121,3434,1,23232])

print sorted(L,key=abs)


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]

def by_score(t):
    return t[1]

L2=sorted(L,key=by_name)
print(L2)
L3=sorted(L,key=by_score)
print(L3)

def calc_prod(lst):
    def lazy_prod():
        def f(x, y):
            return x * y
        return reduce(f, lst)
    return lazy_prod
f = calc_prod([1, 2, 3, 4])
print f()

L = [-1,-2,-3]
def f():
    return abs
a = reduce(L,key=abs)
print a
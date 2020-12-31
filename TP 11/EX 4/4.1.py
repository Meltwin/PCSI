from decimal import *
import time

def fn(x,n,a):
    return x**Decimal(n)-Decimal(a)
def dicho(eps,a0,b0,n,x):
    a = Decimal(a0)
    b = Decimal(b0)
    while Decimal(eps).compare(b-a) == Decimal("-1"):
        m = Decimal((a+b)/Decimal(2))
        if (fn(a,n,x)*fn(m,n,x)<0):
            b = m
        else:
            a = m
        #print(a,b)
    return Decimal((b+a)/Decimal(2))
def racine(a,n):
    r = dicho(10**(-prec+1),0,3,n,a)
    return r
prec = 10
getcontext().prec = prec
print(racine(2,2))
prec = 100
getcontext().prec = prec
print(racine(2,2))
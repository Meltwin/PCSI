## Q1 : Solutions exacte : x = sqrt(2) ou x = - sqrt(2)
## Q2 : f(x)= x² -2

## Q3 : f(0) = -2 ; f(10) = 98
## La fonction f change de signe sur [0,10]

import math
import os
import time
def f(x):
    return x**2 -2
def dicho(eps, a0, b0):
    a = a0
    b = b0
    while (math.fabs(b-a)>eps):
        m = (b+a)/2
        if (f(m)*f(a)<=0):
            b = m
        else:
            a = m
    return (a,b)
def dichoLog(eps, a0, b0):
    c = 0
    a = a0
    b = b0
    while (b - a) > eps:
        c+=1
        m = (a + b) / 2
        if f(a) * f(m) <= 0:
            b = m
        else:
            a = m
        print("a = {}, b= {}".format(a,b))
        time.sleep(0.1)
    return (a,b,c)
a,b = dicho(1E-3,0,2)
print("A 1E-3 près : a={} , b={}".format(a,b))
a,b,c = dichoLog(1E-6,0,2)
print("Nombre d'itération de la boucle : {}".format(c)) ## 21
def fb(x,b):
    return x**2 -b
def racine(x):
    a = 0
    b = 10
    while (math.fabs(b-a)>1E-6):
        m = (b+a)/2
        if (fb(m,x)*fb(a,x)<=0):
            b = m
        else:
            a = m
    print("Racine de {} = {}".format(x,(a+b)/2))
racine(3)
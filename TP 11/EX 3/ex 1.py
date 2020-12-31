import math as mt
import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return mt.sqrt(x)*mt.exp(-2*x)+x-3
x = np.linspace(0,5)
y = [f(k) for k in x]
plt.plot(x,y)
plt.show()

# On peut conjecturer pour f(x)=0 que x = 3

## Résolution par dichotomie
def dicho(eps,a0,b0):
    a = a0
    b = b0
    while(b-a>eps):
        m = (b+a)/2
        if (f(m)*f(a)<0):
            b=m
        else:
            a = m
    return ((a+b)/2)
print(dicho(1E-5,0,5))
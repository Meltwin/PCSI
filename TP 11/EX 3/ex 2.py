import numpy as np
import matplotlib.pyplot as plt
def fn(x,n):
    return (x**n -n*x -1)
x = np.linspace(1,3,1000)
y2 = [fn(k,2) for k in x]
plt.plot(x,y2)
y3 = [fn(k,3) for k in x]
plt.plot(x,y3)
y4 = [fn(k,4) for k in x]
plt.plot(x,y4)
y5 = [fn(k,5) for k in x]
plt.plot(x,y5)
y10 = [fn(k,10) for k in x]
plt.plot(x,y10)
plt.legend(["2","3","4","5","10"])
plt.show()

## Résolution
n = int(input("n : "))
eps = float(input("eps : "))
def dicho(eps, a0,b0,n):
    a = a0
    b = b0
    while (b-a)>eps:
        m = (a+b)/2
        if (fn(a,n)*fn(m,n)<0):
            b = m
        else:
            a = m
    return (b+a)/2
from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt
import math
def f(t):
    return (t**2)*np.exp(-t)
def erreur(x,I):
    return math.log10(math.fabs(x-I))
def gauche(a,b,n):
    s = 0
    for k in range(n):
        s += (b-a)/n * f(a+k*(b-a)/n)
    return s
def milieu(a,b,n):
    s = 0
    for k in range(n):
        s += (b-a)/n * f((2*a+(2*k+1)*(b-a)/n)/2)
    return s
def x(a,b,k):
    return a+k*(b-a)/n
def trapeze(a,b,n):
    s = 0
    d=(b-a)/n
    for i in range(n):
        s+= d*(f(x(a,b,i))+f(x(a,b,i+1)))/2
    return s
n = int(input("N : "))
a = 2
b = 5
eG = []
eM = []
eT = []
I,e= quad(f,a,b)
for i in range(1,n):
    IG = gauche(a,b,i)
    IM = milieu(a,b,i)
    IT = trapeze(a,b,i)
    eG.append(erreur(IG,I))
    eM.append(erreur(IM,I))
    eT.append(erreur(IT,I))
plt.plot(range(1,n),eG)
plt.plot(range(1,n),eM)
plt.plot(range(1,n),eT)
plt.legend(["Gauche","Milieu","Trapèze"])
plt.show()
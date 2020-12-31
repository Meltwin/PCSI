from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt
import math
# x(k) =a+ k*(b-a)/n
n = int(input("N :"))
def f(t):
    return (t**2)*np.exp(-t)
def erreur(x,I):
    return math.log10(math.fabs(x-I))
def gauche(a,b,n):
    s = 0
    for k in range(n):
        s += (b-a)/n * f(a+k*(b-a)/n)
    return s
def droite(a,b,n):
    s = 0
    for k in range(n):
        s += (b-a)/n * f(a+(k+1)*(b-a)/n)
    return s
def milieu(a,b,n):
    s = 0
    for k in range(n):
        s += (b-a)/n * f((2*a+(2*k+1)*(b-a)/n)/2)
    return s
I,e= quad(f,2,5)
eG = []
eD = []
eM = []
for i in range(1,n):
    IG = gauche(2,5,i)
    ID = droite(2,5,i)
    IM = milieu(2,5,i)
    eG.append(erreur(IG,I))
    eD.append(erreur(ID,I))
    eM.append(erreur(IM,I))
# EX 4
plt.plot(range(1,n),eG)
plt.plot(range(1,n),eD)
plt.plot(range(1,n),eM)
plt.legend(["Gauche","Droite","Milieu"])
plt.show()
# EX 5
ab = [math.log10(k) for k in range(1,n)]
plt.plot(ab,eG)
plt.plot(ab,eD)
plt.plot(ab,eM)
plt.legend(["Gauche","Droite","Milieu"])
plt.show()

## EX 6
# Dérivée : f'(t)=2t*exp(-t)-t²*exp(-t)
def df(t):
    return 2*t*np.exp(-t)-(t**2)*np.exp(-t)
ab = np.linspace(2,5,1000)
ordo = [math.fabs(df(k)) for k in ab]
plt.plot(ab,ordo)
plt.show()
# on peut prendre M = 0.16

## b)
def gauchetol(eps,b,a):
    r = math.floor(0.16*((b-a)**2)/eps)+1
    return gauche(a,b,r)
eps = float(input("Eps : "))
print(I)
print(gauchetol(eps,5,2))
import numpy as np
import matplotlib.pyplot as plt
def lagrange(x,i,a):
    Li = 1
    for j in range(len(a)):
        if (i != j):
            Li *= (x-a[j])/(a[i]-a[j])
    return Li
def interpol(x,a,b):
    P = 0
    for i in range(len(a)):
        P += b[i]*lagrange(x,i,a)
    return P

a = np.array([-2,-1, 0, 1, 2])
b = np.array([ 4, 1,-5, 4, 0])
ab = np.linspace(-2.5,2.5)
ordo = [interpol(k,a,b) for k in ab]
plt.plot(ab,ordo)
plt.scatter(a,b)
plt.show()
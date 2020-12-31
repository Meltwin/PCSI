import numpy as np
import matplotlib.pyplot as plt
# vitesse
# Arg : float v0, int k, 
def vitesse(v0,k,m,n,h):
    t = np.zeros(n+1)
    v = np.zeros(n+1)
    v[0] = v0
    
    for i in range(1,n+1):
        t[i] = t[i-1]+h
        v[i] = v[i-1] + h*(9.81-(k/m)*(v[i-1]**2))
    return (t,v)
 
 ## Avec plusieurs pas de temps
"""   
T = 25
pts = 2
Te = T/pts
t,v = vitesse(0,1,1,pts,Te)
plt.plot(t,v)

T = 25
pts = 10
Te = T/pts
t,v = vitesse(0,1,1,pts,Te)
plt.plot(t,v)
"""
T = 25
pts = 100
Te = T/pts
t,v = vitesse(0,1,1,pts,Te)
plt.plot(t,v,color="g")

T = 25
pts = 1000
Te = T/pts
t,v = vitesse(0,1,1,pts,Te)
plt.plot(t,v,color="b")

T = 25
pts = 10000
Te = T/pts
t,v = vitesse(0,1,1,pts,Te)
plt.plot(t,v,color="r")

plt.show()
 ## Avec plusieurs masses
T = 25
pts = 1000
Te = T/pts
t,v = vitesse(0,1,1,pts,Te)
plt.plot(t,v,color="r")

T = 25
pts = 1000
Te = T/pts
t,v = vitesse(0,1,5,pts,Te)
plt.plot(t,v,color="y")
T = 25
pts = 1000
Te = T/pts
t,v = vitesse(0,1,10,pts,Te)
plt.plot(t,v,color="g")

T = 25
pts = 1000
Te = T/pts
t,v = vitesse(0,1,20,pts,Te)
plt.plot(t,v,color="b")

plt.show()
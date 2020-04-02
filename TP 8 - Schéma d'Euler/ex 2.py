## Ex 1 - 3
import matplotlib.pyplot as plt
def eulerListe(h,L,R,U):
    t = [0]
    i = [0]
    k = 0
    while i[k]<=0.95*(U/R):
        t.append(t[k]+h)
        i.append(i[k] +h*(U/L - (R/L)*i[k]))
        k+=1
    t.append(t[k]+h)
    i.append(i[k] +h*(U/L - (R/L)*i[k]))        
    return (t,i)

t,i = eulerListe(0.0001,1,100,1)
plt.plot(t,i)
plt.show()

## Ex 4
import matplotlib.pyplot as plt
import numpy as np
def eulerTableau(n,h,L,R,U):
    t = np.zeros(n+1)
    i = np.zeros(n+1)
    for k in range(1,n+1):
        t[k] = t[k-1] + h
        i[k] = i[k-1] + h*(U/L - (R/L)*i[k-1])
    return (i,t)
    
i,t = eulerTableau(1000,0.0001,1,100,1)
plt.plot(t,i)
plt.show()
## Ex 5
import numpy as np
import matplotlib.pyplot as plt

def eulerTableau(n,h,L,R,U):
    t = np.zeros(n+1)
    i = np.zeros(n+1)
    for k in range(1,n+1):
        t[k] = t[k-1] + h
        i[k] = i[k-1] + h*(U/L - (R/L)*i[k-1])
    return (i,t)
U = 1
R = 100
L = 1
T = 0.1
abs = np.linspace(0,0.1)
ord = [(U/R)*(1-np.exp(-(R/L)*k)) for k in abs]
plt.plot(abs,ord)

def tableVar(periode,p,U,R,L):
    pts = int(periode//p)
    i,t = eulerTableau(pts,p,L,R,U)
    return (i,t)
i,t = tableVar(T,0.0001,U,R,L)
plt.plot(t,i)
i,t = tableVar(T,0.001,U,R,L)
plt.plot(t,i)
i,t = tableVar(T,0.0005,U,R,L)
plt.plot(t,i)
i,t = tableVar(T,0.00001,U,R,L)
plt.plot(t,i)
plt.legend(["Real","p=0.0001","p=0.001","p=0.0005","p=0.00001"])
plt.show()
"""
Les valeurs valides semblent celles inférieures à 0.001ms
"""

## Ex 6
import numpy as np
import matplotlib.pyplot as plt
def eulerMalin(L,R,U):
    tau = L/R
    periode = 3*tau
    n = 1000
    h = periode/n
    
    t = np.zeros(n+1)
    i = np.zeros(n+1)
    for k in range(1,n+1):
        t[k] = t[k-1] + h
        i[k] = i[k-1] + h*(U/L - (R/L)*i[k-1])
    return (i,t)
i,t = eulerMalin(1,100,1)
plt.plot(t,i)

abs = np.linspace(0,0.1)
ord = [(U/R)*(1-np.exp(-(R/L)*k)) for k in abs]
plt.plot(abs,ord)
plt.legend(["Euler Malin","Real"])
plt.show()
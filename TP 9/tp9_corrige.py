 """Correction TP 9"""
 
 """Exercice 1"""
 
 ## Imports
 
 import numpy as np
 import matplotlib.pyplot as plt
 
 ## Exercice 1
 
 # Euler pas de temps h
 
 # v[i+1] = v[i] + h * (g - k/m * v[i] ** 2)
 # t[i+1] = t[i] + h
 
def vitesse(v0, g, k, m, n, h):
    t = np.zeros(n + 1)
    v = np.zeros(n + 1)
    t[0] = 0
    v[0] = v0
    for i in range(0, n):
        v[i+1] = v[i] + h * (g - k/m * v[i] ** 2)
        t[i+1] = t[i] + h
    return (t, v)
    
(t, v) = vitesse(0, 9.81, 1, 1, 1000, 0.001)
plt.plot(t, v)
plt.xlabel("temps (s)")
plt.ylabel("vitesse (m/s)")
plt.grid()
plt.show() 
    
## Impact du pas de temps

(t1, v1) = vitesse(0, 9.81, 1, 1, 1000, 0.001)
(t2, v2) = vitesse(0, 9.81, 1, 1, 100, 0.01)
(t3, v3) = vitesse(0, 9.81, 1, 1, 10, 0.1)
(t4, v4) = vitesse(0, 9.81, 1, 1, 5, 0.2)
(t5, v5) = vitesse(0, 9.81, 1, 1, 4, 0.25)

plt.plot(t1, v1)
plt.plot(t2, v2)
plt.plot(t3, v3)
plt.plot(t4, v4)
plt.plot(t5, v5)
plt.xlabel("temps (s)")
plt.ylabel("vitesse (m/s)")
plt.legend(["h = 1ms", "h = 10ms", "h = 100ms", "h = 200ms", "h = 250ms"])
plt.title("Influence du pas de temps")
plt.grid()
plt.show()

## Impact de la masse

(t1, v1) = vitesse(0, 9.81, 1, 1, 1500, 0.001)
(t2, v2) = vitesse(0, 9.81, 1, 2, 1500, 0.001)
(t3, v3) = vitesse(0, 9.81, 1, 4, 1500, 0.001)
(t4, v4) = vitesse(0, 9.81, 1, 8, 1500, 0.001)
(t5, v5) = vitesse(0, 9.81, 1, 16, 1500, 0.001)

plt.plot(t1, v1)
plt.plot(t2, v2)
plt.plot(t3, v3)
plt.plot(t4, v4)
plt.plot(t5, v5)
plt.xlabel("temps (s)")
plt.ylabel("vitesse (m/s)")
plt.title("Influence de la masse")
plt.legend(["m = 1kg", "m = 2kg", "m = 4kg", "m = 8kg", "m = 16kg"])
plt.grid()
plt.show()

## Exercice 2

# Schema d'Euler pas de temps h
# i[k+1] = i[k] + h * (U/L - R/L * i[k])
# t[k+1] = t[k] + h

def eulerListe(h, L, R, U):
    t = 0
    i = 0
    tl = [0]
    il = [0]
    while i <= 0.95 * U / R:
        t = t + h
        i = i + h * (U/L - R/L * i)
        tl.append(t)
        il.append(i)
    return (tl, il)

(t, i) = eulerListe(0.1E-3, 1, 100, 2)
plt.plot(t, i)
plt.xlabel("Temps (s)")
plt.ylabel("Intensite (A)")
plt.title("Etablissement du courant dans une bobine")
plt.grid()
plt.show()

## Version tableau

def eulerTableau(n, h, L, R, U):
    t = np.zeros(n + 1)
    i = np.zeros(n + 1)
    t[0] = 0
    i[0] = 0
    for k in range(0, n):
        i[k+1] = i[k] + h * (U/L - R/L * i[k])
        t[k+1] = t[k] + h
    return (t, i)

(t, i) = eulerTableau(200,0.1E-3, 1, 100, 2)
plt.plot(t, i)
plt.xlabel("Temps (s)")
plt.ylabel("Intensite (A)")
plt.title("Etablissement du courant dans une bobine")
plt.grid()
plt.show()

## Comparaison avec la solution exacte

(t1, i1) = eulerTableau(200, 0.1E-3, 1, 100, 2)
(t2, i2) = eulerTableau(10, 0.002, 1,  100, 2)
(t3, i3) = eulerTableau(2, 0.01, 1, 100, 2)

U = 2
L = 1
R = 100
t4 = np.linspace(0, 0.02, 1000)
i4 = U/R *( 1 - np.exp(-R/L*t4))
plt.plot(t1,i1)
plt.plot(t2,i2)
plt.plot(t3,i3)
plt.plot(t4,i4)
plt.legend(["Euler 0.1ms", "Euler 2ms", "Euler 10ms", "Exact"])
plt.grid()
plt.xlabel("Temps (s)")
plt.ylabel("Intensite (A)")
plt.title("Etablissement du courant dans une bobine")
plt.show()

## Choix du pas de temps malin

def eulerMalin(L, R, U):
    h = (L / R) / 100 #1/100 de la constante de temps
    t = 0
    i = 0
    tl = [0]
    il = [0]
    while i <= 0.95 * U / R:
        t = t + h
        i = i + h * (U/L - R/L * i)
        tl.append(t)
        il.append(i)
    return (tl, il)

(t, i) = eulerMalin(1, 100, 2)
plt.plot(t, i)
plt.xlabel("Temps (s)")
plt.ylabel("Intensite (A)")
plt.title("Etablissement du courant dans une bobine")
plt.grid()
plt.show()
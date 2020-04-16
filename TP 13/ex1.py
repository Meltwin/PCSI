import numpy as np
import matplotlib.pyplot as plt
import math
fichier = open("D:/Dev/Python/PCSI/TP 13/data.txt", "r")
lignes = fichier.readlines() 
fichier.close()

taille= np.zeros(len(lignes))
poids = np.zeros(len(lignes))

for i in range(len(lignes)):
    t = lignes[i].split()
    taille[i] = t[0]
    poids[i] = t[1]

# Input float[] t
def moyenne(t):
    s=0.0
    for v in t:
        s +=v
    s = s/len(t)
    return s
tbar = moyenne(taille)
pbar = moyenne(poids)
print(tbar,pbar)

def variance(t,moy):
    s = 0.0
    for v in t:
        s += (v-moy)**2
    s = s/(len(t)-1)
    return s
st2=variance(taille,tbar)
sp2=variance(poids,pbar)
print(st2,sp2)

def covariance(tA,moyA, tB,moyB):
    s=0
    for i in range(len(tA)):
        s += (tA[i]-moyA)*(tB[i]-moyB)
    s = s/(len(tA)-1)
    return s
stp = covariance(taille,tbar, poids,pbar)


# Régression linénaire
a = stp/st2
b = pbar - a*tbar

plt.scatter(taille,poids) # Raw imported data 
m = min(taille)
M = max(taille)
ab = np.linspace(m,M,1000)
ordo = [a*k+b for k in ab]
plt.plot(ab,ordo,color="R")
plt.xlabel("Taille (cm)")
plt.ylabel("Poids (kg)")
plt.show()

def coeffDeterm(coVar,varA,varB):
    return (coVar**2)/(varA*varB)
print(coeffDeterm(stp,st2,sp2)) # 0.6
import numpy as np
import random as rd
import matplotlib.pyplot as plt
N = 300
Ngrain = 10000
C = 1.0
P = 1
piles = np.zeros(N+1)
# tombe_pile: applique la loi aux piles de grain
# Arg : int[] piles
# Retour : int[] r le tableau modifié
def tombe_pile():
    global piles
    global P
    global C
    nbDeplace = 0
    for i in range(len(piles)-1):
        h = piles[i]-piles[i+1]
        if (h>P):
            nbGrain = P*((int)((h/P+C)/C*rd.random())+1)
            piles[i] -= nbGrain
            piles[i+1] += nbGrain
            nbDeplace += nbGrain
    return nbDeplace

for e in range(Ngrain):
    piles[0] += P
    tombe_pile()
plt.bar(range(0,N+1),piles)
plt.show()

## Nb de grains déplacés
import numpy as np
import random as rd
import matplotlib.pyplot as plt
N = 300
Ngrain = 10000
C = 2.0
P = 1.0
piles = np.zeros(N+1)
NGrains = np.zeros(Ngrain)
# tombe_pile: applique la loi aux piles de grain
# Arg : int[] piles
# Retour : int[] r le tableau modifié
def tombe_pile():
    global piles
    global P
    global C
    nbDeplace = 0
    for i in range(len(piles)-1):
        h = piles[i]-piles[i+1]
        if (h>P):
            nbGrain = P*((int)((h/P+C)/C*rd.random())+1)
            piles[i] -= nbGrain
            piles[i+1] += nbGrain
            nbDeplace += nbGrain
    return nbDeplace

for e in range(Ngrain):
    piles[0] += P
    dep = tombe_pile()
    NGrains[int(dep)] += +1
plt.bar(range(Ngrain),NGrains)
plt.show()

## P = la force de gravité ? => AUGMENTE la taille
## C est responsable de l'aléatoire => diminue le relief
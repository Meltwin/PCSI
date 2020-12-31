import numpy as np
import matplotlib.pyplot as plt
# nouvel_etat : change l'état des cellules du tableau
# Argument : int[] t
# Retour : int[] r, le tableau modifié
def nouvel_etat(t):
    r = np.zeros(len(t))
    if (t[1] == 1):
        r[0] = 1
    else :
        r[0] = 0
    if (t[-2]==1):
        r[-1] = 1
    else:
        r[-1] = 0
        
    for i in range(1,len(t)-1):
        if (t[i-1] == 1 or t[i+1] == 1):
            r[i] = 1
    return r
N = 10
T= np.zeros([N,2*N+1])
T[0][N] = 1
for i in range(N-1):
    T[i+1] = nouvel_etat(T[i])
plt.imshow(T,cmap="binary",interpolation="nearest")
plt.show()

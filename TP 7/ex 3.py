import numpy as np
import matplotlib.pyplot as plt
# nouvel_etat2 : change l'état des cellules du tableau en fonction du code
# Argument : int code, int[] t
# Retour : int[] r, le tableau modifié
def nouvel_etat2(code,t):
    r = np.zeros(len(t))
    r[0] = t[0]
    r[-1] = t[-1]
    for i in range(1,len(t)-1):
        combinaison = t[i-1]*4+t[i]*2+t[i+1]
        r[i] = (code//(2**combinaison))%2
    return r
"""
base = np.array([0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0])
for i in range(10):
    base = nouvel_etat(base)
    print("Etape {0} : {1}".format(i+1,base))
""" 
N = 400
T= np.zeros([N,2*N+1])
T[0][2*N-1] = 1
for i in range(N-1):
    T[i+1] = nouvel_etat2(11,T[i])
print(T)
plt.imshow(T,cmap="binary",interpolation="nearest")
plt.show()

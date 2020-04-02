import numpy as np
t = np.array([15,3,9,1,64,12,7,3,16,10,3,2,18,1,21])
## Exercice 1 - Somme des termes
s = 0
for i in range(len(t)):
    s +=t[i]
print(s)
## Exercice 2 - Moyenne 
s = 0
for i in range(len(t)):
    s +=t[i]
print(s/len(t))
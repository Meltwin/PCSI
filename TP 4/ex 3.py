import numpy as np
t = np.array([15,3,9,1,64,12,7,3,16,10,3,2,18,1,21])
## Return Max value
m = 0
for i in range(len(t)):
    if (t[i] >m):
        m = t[i]
print("La valeur maximal est : {}".format(m))
## Return first key of Max value 
m = 0
id = 0
for i in range(len(t)):
    if (t[i] >m):
        m = t[i]
        id = i
print("La valeur maximal (1er occurence) est : {0} dans la case {1}".format(m,id))
## Return last key of Max value 
m = 0
id = 0
for i in range(len(t)):
    if (t[i] >=m):
        m = t[i]
        id = i
print("La valeur maximal (dernière occurence) est : {0} dans la case {1}".format(m,id))
## Show local max
for i in range(1,len(t)-1):
    if (t[i]>t[i-1] and t[i]>t[i+1]):
        print(t[i])
import numpy as np
t = np.array([5,6,4,3,5,6,4,3,5,6,4,3,5,6])
## p given, test if p-periodic
p = int(input("Période : "))
b = True
for i in range(len(t)-p):
    if not(t[i] == t[i+p]):
        b=False
print(b)
## Search p from table
t = np.array([5,6,4,3,5,6,4,3,5,6,4,3,5,6])
b = False
for p in range(1,len(t)):
    if not(b):    
        tB = True
        for i in range(len(t)-p):
            if not(t[i] == t[i+p]):
                tB=False
        if tB:
            b=True
            print("La période est : {}".format(p))
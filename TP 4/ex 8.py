## 1 - From bits to digit
t = eval(input("Octet : "))
d = 0
for i in range(8):
    d += t[i]*(2**(i))
print(d)
## 2 - From digit to bits
import numpy as np 
d = int(input("Nombre : "))
t = np.zeros(8)
for i in range(7,-1,-1):
    if (d>=(2**i)):
        t[i] = 1
        d -= (2**i)
print(t)
## 3 - Rotation droite
import numpy as np
t = eval(input("Tableau : "))
last = t[len(t)-1]
for i in range(len(t)-1,0,-1):
    t[i] = t[i-1]
t[0] = last
print(t)
## 4 - Test conjugué
import numpy as np

# Init
nA = int(input("Nombre 1 : "))
nB = int(input("Nombre 2 : "))

def setInBinary(d):
    t = np.zeros(8)
    for i in range(7,-1,-1):
        if (d>=(2**i)):
            t[i] = 1
            d -= (2**i)
    return t
tA = setInBinary(nA)
tB = setInBinary(nB)

# Set Functions

def isEqual(ta,tb):
    b = True
    for i in range(len(ta)):
        if not(ta[i] == tb[i]):
            b=False
            break
    return b
def rotateB():
    global tB
    last = tB[len(tB)-1]
    for i in range(len(tB)-1,0,-1):
        tB[i] = tB[i-1]
    tB[0] = last

# Calc
b = False
for i in range(8):
    print(tA)
    print(tB)
    print()
    if not(isEqual(tA,tB)):
        rotateB()
    else:
        b = True
        break
print(b)

## 5 - All Conjugués to n 
import numpy as np

# Init
n = int(input("N = "))

def setInBinary(d):
    t = np.zeros(8)
    for i in range(7,-1,-1):
        if (d>=(2**i)):
            t[i] = 1
            d -= (2**i)
    return t

tA = setInBinary(n)
tB = []

# Set Functions

def isEqual(ta,tb):
    b = True
    for i in range(len(ta)):
        if not(ta[i] == tb[i]):
            b=False
            break
    return b
def rotateB():
    global tB
    last = tB[len(tB)-1]
    for i in range(len(tB)-1,0,-1):
        tB[i] = tB[i-1]
    tB[0] = last

for nB in range(256):
    tB = setInBinary(nB)
    
    b = False
    for i in range(8):
        if not(isEqual(tA,tB)):
            rotateB()
        else:
            b = True
            break
    if b:
        print("N = {0} et N' = {1} sont conjugués".format(n,nB))
        """
        print("N = {}".format(tA))
        print("N' = {}".format(setInBinary(nB)))
        print()
        """
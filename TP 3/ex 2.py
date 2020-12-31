import math
## Somme 1
n = int(input("N : "))
s = 0
for k in range(1,n+1):
    r = 1
    for p in range(1,k**2+1):
        r *= math.cos(p)
    s+=r
print(s)
## Somme 2
n = int(input("N ="))
s = 0
for k in range(1,n+1):
    s += math.factorial(k)
print(s)
## Somme 3
n=int(input("N = "))
r = 1
for k in range(1,n+1):
    s = 0
    for p in range(1,k+1):
        s += p
    r *= s
print(r)
## Somme 4
n = int(input("N = "))
s = 0
for k in range(2,n+1,2):
    s += k**3
print(s)
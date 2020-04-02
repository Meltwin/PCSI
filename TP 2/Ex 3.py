import math
## Somme 1 - somme de k
n = int(input("N = "))
s = 0
for i in range(1,n+1):
    s += i
print(s)

## Somme 2 - somme de k²
n = int(input("N = "))
s = 0
for i in range(1,n+1):
    s += i**2
print(s)

## Somme 3 - somme de k^α
n = int(input("N = "))
a = int(input("α = "))
s = 0
for i in range(1,n+1):
    s += i**a
print(s)

## Somme 4 - somme de cos(k)
n = int(input("N = "))
s = 0
for i in range(1,n+1):
    s += math.cos(i)
print(s)
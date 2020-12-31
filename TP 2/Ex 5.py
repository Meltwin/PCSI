import math
## Somme 1
n = int(input("N = "))
s = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        s += i+j
print(s)

## Somme 2
n = int(input("N = "))
s = 0
for i in range(0,n+1):
    for j in range(1,n+1):
        s += math.cos(i*(math.pi)/3)*math.sin(j*(math.pi)/3)
print(s)

## Somme 3
n = int(input("N = "))
s = 0
for i in range(1,n+1):
    for j in range(i,n+1):
        s += i/j
print(s)

## Somme 3
n = int(input("N = "))
s = 0
for i in range(1,n+1):
    for j in range(i,n+1):
        s += i/j
print(s)

## Somme 4
n = int(input("N = "))
s = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i>=j):
            s += i
        else :
            s += j
print(s)

## Somme 4 - Alternativen = int(input("N = "))
n = int(input("N = "))
s = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        s += max(i,j)
print(s)
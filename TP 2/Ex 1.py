## Question 1 - Rang n
import math

n = int(input("N = "))
u = 2**0.5
for i in range(1, n+1):
    u = math.sqrt(2 - u)
print(u)

## Question 2 - Tout jusqu'à n
import math

n = int(input("N = "))
u = 2**0.5
print("U0 = "+str(u))
for i in range(1, n+1):
    u = math.sqrt(2 - u)
    print("U"+str(i)+" = "+str(u))
    
"""
La suite u(n) a l'air de tendre vers 1 lorsque n tend vers plus l'infini
"""

## Question 3 - Rangs Pairs
import math

n = int(input("N = "))
u = 2**0.5
print("U0 = "+str(u))
for i in range(1, n+1):
    u = math.sqrt(2 - u)
    if(i%2 == 0):
        print("U"+str(i)+" = "+str(u))

## Question 3 - Rangs Impairs
import math

n = int(input("N = "))
u = 2**0.5
print("U0 = "+str(u))
for i in range(1, n+1):
    u = math.sqrt(2 - u)
    if(i%2 ==1):
        print("U"+str(i)+" = "+str(u))

## Question 4 - Seuil
import math

e = float(input("ε = "))
u = 2**0.5
m = 0
while (math.fabs(u-1) >= e):
    m += 1
    u = math.sqrt(2 - u)
print(m)


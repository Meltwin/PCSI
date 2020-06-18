## Q1 : u(n+1) = u(n) - (x²-2)/2x et u0 = 10

import math

eps = float(input("Précision : "))
u0 = 10
u = [u0]
def f(x):
    return x**2 - 2
def df(x):
    return 2*x
u.append(u0-f(u0)/df(u0))
k = 1
while math.fabs(u[k]-u[k-1])>eps:
    u.append(u[k]-f(u[k])/df(u[k]))
    k +=1
print(u[-1])

"""
Print all terms
"""
for k in range(len(u)):
    print("{} : {}".format(k,u[k]))
print("Nombre d'itération : {}".format(len(u)-1)) # 7
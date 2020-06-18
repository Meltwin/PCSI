import math
def fn(x,n):
    return (x**n -n*x -1)
def dfn(x,n):
    return (n*(x**(n-1))-n)
n = int(input("n : "))
eps = float(input("eps : "))
def newton(eps, u0,n):
    u = [u0]
    u.append(u0-fn(u0,n)/dfn(u0,n))
    k = 1
    while math.fabs(u[k]-u[k-1])>eps:
        u.append(u[k]-fn(u[k],n)/dfn(u[k],n))
        k+=1
    return u[-1]
print(newton(eps,3,n))
print(newton(eps,0.5,n))
print(newton(eps,-4,n))
# On trouve plusieurs valeurs, car l'équation peut en accepter en dehors de [1,3]
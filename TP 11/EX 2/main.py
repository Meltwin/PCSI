## Q1 : u(n+1) = u(n) - (x²-2)/2x et u0 = 10
u0 = 10

n = int(input("Entrez le rang voulu : "))
u = u0
def f(x):
    return x**2 - 2
def df(x):
    return 2*x
for k in range(n):
    u = u - f(u)/df(u)
print(u)

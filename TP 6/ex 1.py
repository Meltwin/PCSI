# f
# Arg : réel x
# Retourne : un réel égal à (1-x)*sqrt(1-x**2)
def f(x):
    return (1-x)*((1-x**2)**0.5)
# g
# Arg : réel x
# Retourne : un réel x**3 / x**2 + 1
def g(x):
    return (x**3)/(x**2 +1)
# h
# Arg : réel x
# Retourne : un réel égal à f(x)-g(x)
def h(x):
    return f(x)-g(x)
    
## Affichages calculs
print(f(1/1))
print(g(1/2))
print(h(1/2))
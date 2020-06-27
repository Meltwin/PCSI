## TP 11

## Exercice 1

## Q4

def f(x):
    y = x ** 2 - 2
    return y

a = 0
b = 10
eps = 0.001

while (b - a) > eps:
    m = (a + b) / 2
    if f(a) * f(m) <= 0:
        b = m
    else:
        a = m

print(a, b)

## Q5

a = 0
b = 10
eps = 1E-6 # ou 10 ** (-6)
c = 0 # compteur

while (b - a) > eps:
    c = c + 1
    m = (a + b) / 2
    if f(a) * f(m) <= 0:
        b = m
    else:
        a = m
    print (a, b)

print(a, b)
print("Nombre d'itérations", c)

## Q6

# Fonction qui prend en entrée u > 0 et qui
# retourne racine(u)

def racine(u):
    
    def f(x):
        y = x ** 2 - u
        return y
    
    a = 0
    b = u + 1
    eps = 1E-6
    while (b - a) > eps:
        m = (a + b) / 2
        if f(a) * f(m) <= 0:
            b = m
        else:
            a = m
    return b
    
## Exercice 2

## Q1

# Newton :
# u(n+1) = u(n) - (u(n) ** 2 - 2)/(2 * u(n))

## Q2

n = int(input("Entrez n : "))
u = 10 # u0
for i in range(0, n):
    u = u - (u ** 2 - 2)/(2 * u)
    print(u)
print(u)

## Q3

eps = float(input("Entrez epsilon : "))
u = 10 # u0
v = u + 2 * eps
while abs(u - v) > eps:
    v = u
    u = u - (u ** 2 - 2)/(2 * u)
    print(u)


## Exercices

## Exercice 1
import numpy as np

## Q1
def f(x):
    y = np.sqrt(x) * np.exp(-2 * x) + x - 3
    return y
 
## Q2 
import matplotlib.pyplot as plt

absc = np.linspace(0, 5, 1000)
ordo = f(absc)

plt.plot(absc, ordo)
plt.show()

## OU

x = np.linspace(0, 5, 1000)
plt.plot(x, f(x))
plt.grid()
plt.show()

## Q3

# Il n'y a l'air d'avoir qu'une solution comprise entre 0 et 5

## Q4

a = 0
b = 5
eps = 1E-5

while (b - a) > eps:
    m = (a + b) / 2
    if f(a) * f(m) <= 0:
        b = m
    else:
        a = m
print(a, b)

## Exercice 2

## Q1

def f(x, n):
    y = x ** n - n * x - 1
    return y
    
## Solution basique
    
x = np.linspace(-0.5, 1.5, 1000)
plt.plot(x, f(2, x))
plt.plot(x, f(3, x))
plt.plot(x, f(4, x))
plt.plot(x, f(5, x))
plt.show()

## Solution plus avancée (pas vu en cours)

x = np.linspace(-0.5, 1.5, 1000)
for n in [2, 3, 4, 5]:
    plt.plot(x, f(n, x))
plt.show()

## Q2

# Faire l'étude mathématique de la fonction
# (derivée + variations)

## Q3

# Méthode de Newton
# f(x) = x^n - nx - 1
# f'(x) = nx^{n - 1} - n = n (x^{n - 1} - 1)
#
# On pose donc
# u(n+1) = u(n) - f(u(n))/f'(u(n))
# u(n+1) = u(n) - (u(n)^n - n u(n) - 1) / ( n * (u(n)^(n - 1) - 1))

n = int(input("Entrez n : "))
u = 2 # D'apres la question precedente on est dans [1, 3] je choisis un point au milieu

for k in range(0, 10): # 10 itérations (arbitaire)
    u = u - f(u, n) / (n * (u ** (n - 1) - 1))
print(u)
    
# Pour n = 3, on trouve 1.87 je verifie en tracant la courbe
x = np.linspace(1, 3, 100)
plt.plot(x, f(x, 3))
plt.show()
# c'est cohérent

## Q5

# On trouve des valeurs differentes car
# l'equation f(x) = 0 a pluisieurs solutions pour
# n = 3 (faire le tracé). On ne sait pas vers
# laquelle Newton va converger.
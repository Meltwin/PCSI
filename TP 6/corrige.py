## Imports

import numpy as np
import matplotlib.pyplot as plt

## Exercice 1

def f(x):
    y = (1 - x) * np.sqrt(1 - x * x)
    return y

def g(x):
    y = (x ** 3) / (x ** 2 + 1)
    return y

def h(x):
    y = f(x) - g(x)
    return y

## Exercice 2

## Q3

x = np.linspace(-1, 1, 100)
plt.plot(x, f(x))
plt.show()

## Q4
x = np.linspace(-1, 1, 100)
plt.plot(x, f(x), x, g(x), x, h(x))
plt.legend(["f", "g", "h"])
plt.show()

## Exercice 3

def f(alpha, t):
    y = - np.cos(t) + alpha * np.sin(t)
    return y

t = np.linspace(0, np.pi, 100)
for a in range(-2, 3):
    plt.plot(t, f(a, t))
plt.show()

## Exercice 4

def volumeCube(x):
    v = x * x * x
    return v

def volumeTetra(x):
    v = x * x * x / (6 * np.sqrt(2))
    return v

def volumeBoule(d):
    v = np.pi / 6 * volumeCube(d)
    return v

x = float(input("Entrez x : "))
print("Volume cube ", volumeCube(x))
print("Volume tetraedre ", volumeTetra(x))
print("Volume boule ", volumeBoule(x))

## Exercice 5

# somme(t) : calcule la somme des cases du tableau t
# argument : t un tableau d'entiers
# retourne : la somme (entier)

def somme(t):
    n = len(t)
    S = 0
    for i in range(0, n):
        S = S + t[i]
    return S

# Test :
t = np.array([1, 3, 5, 1])
print(somme(t))

# moyenne(t) : calcule la moyenne des cases du tableau t
# argument : t un tableau d'entiers
# retourne : la moyenne (float)

def moyenne(t)
    n = len(t)
    s = somme(t) # on utilise la fonction précédente
    moy = n / s
    return moy

## Exercice 6

# min(t) : retourne la valeur minimale d'un tableau
# argument : t un tableau d'entiers non vide
# retourne : la valeur min (entier)

def min(t):
    n =  len(t)
    res = t[0] 
    for i in range(1, n):
        if t[i] < res:
            res = t[i]
    return res

# argmin(t) : retourne l'indice de la première case minimale
# argument : t un tableau d'entiers
# retourne : l'indice (entier)

def argmin(t):
    n =  len(t)
    minimal = t[0]
    pos = 0
    for i in range(1, n):
        if t[i] < minimal:
            minimal = t[i]
            pos = i
    return pos

## Exercice 7

def tri_croissant(t):
    n = len(t)
    res = True
    for i in range(0, n - 1):
        if t[i] > t[i + 1]:
            res = False
    return res

## Exercice 8

def distance(xa, ya, xb, yb):
    d = ((xb - xa) ** 2 + (yb - ya) ** 2) ** 0.5
    return d

def longueur(absc, ordo):
    n = len(absc)
    somme = 0
    for i in range(0, n-1):
        d = distance(absc[i], ordo[i], absc[i+1], ordo[i+1])
        somme = somme + d
    return somme

## Q3
# Les racine niemes de l'unite forment un polygone regulier

n = int(input("n = "))
absc = np.zeros(n + 1) # un point de plus pour boucler
ordo = np.zeros(n + 1)
for k in range(0, n + 1):
    absc[k] = np.cos(2 * np.pi * k / n)
    ordo[k] = np.sin(2 * np.pi * k / n)
perimetre = longueur(absc, ordo)
print(perimetre)


## Exercice 9

def carre(n):
    ligne = ""
    for i in range(0, n):
        ligne = ligne + "*"
    for k in range(0, n):
        print(ligne)

def pyramide(n):
    ligne = ""
    for i in range(0, n):
        ligne = ligne + "*"
        print(ligne)

## Exercice 11

# fib(n) : calcule un
# argument : n un entier > 1
def fib(n):
    t = np.zerps(n+1)
    t[0] = 0
    t[1] = 1
    for k in range(2, n+1):
        t[k] = t[k-1] + t[k-2]
    return t[n]


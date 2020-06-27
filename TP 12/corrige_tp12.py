## TP 12 : Calcul d'intégrales

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

## Utilisation de quad

def f(t):
    y = np.exp(t)/(t ** 2 + 1)
    return y

(I, e) = quad(f, 0, 2)
print(I)
print(e)

## Partie 2

## Q2

def f(t):
    y = t ** 2 * np.exp(-t)
    return y
    
a = 2
b = 5
n = int(input("Combien de rectangles ? "))

d = (b - a) / n

S = 0
for k in range(0, n):
    S = S + d * f(a + k * d)
print(S)

## Q3

# retourne une approximation de l'integrale avec n rectangles
# a gauche
def gauche(n):
    a = 2
    b = 5
    
    d = (b - a) / n
    
    S = 0
    for k in range(0, n):
        S = S + d * f(a + k * d)
    return(S)
    
def droite(n):
    a = 2
    b = 5
    
    d = (b - a) / n
    
    S = 0
    for k in range(0, n):
        S = S + d * f( a + (k+1) * d )
    return(S)

def milieu(n):
    a = 2
    b = 5
    
    d = (b - a) / n
    
    S = 0
    for k in range(0, n):
        gauche = a + k * d
        droite = a + (k + 1) * d
        S = S + d * f((gauche + droite) / 2 ) # moyenne a l'interieur
    return(S)
    
# pas demandé mais on le fait quand meme

def trapeze(n):
    a = 2
    b = 5
    
    d = (b - a) / n
    
    S = 0
    for k in range(0, n):
        gauche = a + k * d
        droite = a + (k + 1) * d
        S = S + d * (f(gauche) + f(droite)) / 2 # moyenne a l'exterieur
    return(S)
    
# On constate qu'avec 50 rectangles/trapezes les méthodes milieu et trapèze sont plus précises que gauche et droite

# Remarque : la méthode des trapèzes correspond à la moyenne
# des methodes gauche et droite :
# trapeze(n) = (gauche(n) + droite(n))/2

## Q4

(I, e) = quad(f, 2, 5)

# Fonctions d'erreur (en log)
def errg(n):
    y = np.log10(abs(I - gauche(n)))
    return y
    
def errd(n):
    y = np.log10(abs(I - droite(n)))
    return y
    
def errm(n):
    y = np.log10(abs(I - milieu(n)))
    return y
    
def errt(n):
    y = np.log10(abs(I - trapeze(n)))
    return y
    
    
N = 50

# pour la courbe gauche
x = np.zeros(N)
y = np.zeros(N)
for k in range(0, N):
    x[k] = k + 1 # le nombre de rect va de 1 à N
    y[k] = errg(k + 1)

plt.plot(x, y, label = 'gauche')

# pour la courbe droite
x = np.zeros(N)
y = np.zeros(N)
for k in range(0, N):
    x[k] = k + 1 # le nombre de rect va de 1 à N
    y[k] = errd(k + 1)

plt.plot(x, y, label = 'droite')

# pour la courbe du milieu
x = np.zeros(N)
y = np.zeros(N)
for k in range(0, N):
    x[k] = k + 1 # le nombre de rect va de 1 à N
    y[k] = errm(k + 1)

plt.plot(x, y, label = 'milieu')

# pour la courbe du trapeze
x = np.zeros(N)
y = np.zeros(N)
for k in range(0, N):
    x[k] = k + 1 # le nombre de rect va de 1 à N
    y[k] = errt(k + 1)

plt.plot(x, y, label = 'trapèze')

plt.legend()
plt.xlabel("Nombre de rectangles/trapèzes")
plt.ylabel("Erreur logarithmique")
plt.title("Vitesse de convergence des differentes méthodes")
plt.grid()
plt.show()
    
    
## Question 5 : en echelle log-log

N = 50

# pour la courbe gauche
x = np.zeros(N)
y = np.zeros(N)
for k in range(0, N):
    x[k] = np.log10(k + 1) # le nombre de rect va de 1 à N
    y[k] = errg(k + 1)

plt.plot(x, y, label = 'gauche')

# pour la courbe droite
x = np.zeros(N)
y = np.zeros(N)
for k in range(0, N):
    x[k] = np.log10(k + 1) # le nombre de rect va de 1 à N
    y[k] = errd(k + 1)

plt.plot(x, y, label = 'droite')

# pour la courbe du milieu
x = np.zeros(N)
y = np.zeros(N)
for k in range(0, N):
    x[k] = np.log10(k + 1) # le nombre de rect va de 1 à N
    y[k] = errm(k + 1)

plt.plot(x, y, label = 'milieu')

# pour la courbe du trapeze
x = np.zeros(N)
y = np.zeros(N)
for k in range(0, N):
    x[k] = np.log10(k + 1) # le nombre de rect va de 1 à N
    y[k] = errt(k + 1)

plt.plot(x, y, label = 'trapèze')
plt.legend()
plt.xlabel("log(Nombre de rectangles/trapèzes)")
plt.ylabel("Erreur logarithmique")
plt.title("Vitesse de convergence des differentes méthodes")
plt.grid()
plt.show()
    
## PARTIE 3 : méthode des trapèzes

# déjà programmé dans la partie 2

    
    
    
    
    
    
    
    






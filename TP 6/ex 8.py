# distance : retourne la distance entre deux points
# Arg : entier xa, entier ya, entier xb, entier yb
# Retourne : un int : sqrt((xb-xa)**2 + (yb-ya)**2)
def distance(xa,ya,xb,yb):
    return ((xb-xa)**2 + (yb-ya)**2)**0.5
# longueur : retourne la longueur d'une ligne polygonale
# Arg : table abs, table ord
# Retourne : un int : somme(i=1,len(abs),distance(abs[i-1],ord[i-1],abs[i],ord[i])
def longueur(abs,ord):
    s = 0
    for i in range(1,len(t)):
        s += distance(abs[i-1],ord[i-1],abs[i],ord[i])
    return s
    
## Programme polygone a n côté dans le cercle unité
import numpy as np
# angles : retourne la liste des angles entre Ox et OM avec M le point
# Arg : un entier n 
# Retourne : un tableau de taille n avec tous les angles
def angles(n):
    a = []
    for i in range(n):
        a.append(i*(2*np.pi/n))
    return a
# pos : créé la liste des positions des points à partir des angles
# Arg : un tableau a
# Retourne : un tableau [abs,ord]
def pos(a):
    abs = []
    ord = []
    for i in range(len(a)):
        abs.append(np.cos(a[i]))
        ord.append(np.sin(a[i]))
    return [abs,ord]
# distance : retourne la distance entre deux points
# Arg : entier xa, entier ya, entier xb, entier yb
# Retourne : un int : sqrt((xb-xa)**2 + (yb-ya)**2)
def distance(xa,ya,xb,yb):
    return ((xb-xa)**2 + (yb-ya)**2)**0.5
# longueur : retourne la longueur d'une ligne polygonale
# Arg : table abs, table ord
# Retourne : un int : somme(i=1,len(abs),distance(abs[i-1],ord[i-1],abs[i],ord[i])
def longueur(abs,ord):
    s = 0
    for i in range(1,len(abs)):
        s += distance(abs[i-1],ord[i-1],abs[i],ord[i])
    return s
n = int(input("Polygone à n côté, n="))
pos = pos(angles(n))
print("Longueur = {}".format(longueur(pos[0],pos[1])))
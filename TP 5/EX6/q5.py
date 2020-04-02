import random
print("\n|| Algo simulation de n lancées de m dé ||",end="\n\n")
# Init des variables
n = int(input("Nombre de lancées : "))
m = int(input("Nombre de dés par lancée : "))
paires = []
s= 0
# Simulation des lancées de dé
for i in range(n):
    d = 0
    for j in range(m):
        d += random.randint(1,6)
    s+= d
    paires.append(d)
# Calcul de la moyenne 
k = s/n
# Résultats
print("Lancées : {}".format(paires))
print("Moyenne : {}".format(k))
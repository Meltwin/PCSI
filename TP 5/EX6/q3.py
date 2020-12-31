import random
print("\n|| Algo simulation de n lancées de 2 dé ||",end="\n\n")
# Init des variables
n = int(input("Nombre de lancées : "))
paires = []
s= 0
# Simulation des lancées de dé
for i in range(n):
    dA = random.randint(1,6)
    dB = random.randint(1,6)
    s += dA+dB
    paires.append(dA + dB)
# Calcul de la moyenne 
m = s/n
# Résultats
print("Lancées : {}".format(paires))
print("Moyenne : {}".format(m))
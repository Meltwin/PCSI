import random
print("\n|| Algo distribution sur n lancées de 2 dé ||",end="\n\n")
# Init des variables
n = int(input("Nombre de lancées : "))
paires = []
distribution = [0]*12
s= 0
# Simulation des lancées de dé
for i in range(n):
    dA = random.randint(1,6)
    dB = random.randint(1,6)
    s+= dA+dB
    distribution[dA+dB-1] += 1
    paires.append(dA+dB)
# Calcul de la moyenne 
m = s/n
# Résultats
print("Lancées : {}".format(paires))
print("Distribution : {}".format(distribution))
print("Moyenne : {}".format(m))
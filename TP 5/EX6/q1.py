import random
print("\n|| Algo simulation de n lancées de 1 dé ||",end="\n\n")
# Init des variables
n = int(input("Nombre de lancées : "))
l = []

# Simulation des lancées de dé
for i in range(n):
    l.append(random.randint(1,6))
# Résultats
print(l)
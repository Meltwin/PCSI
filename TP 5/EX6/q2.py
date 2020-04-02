import random
print("\n|| Moyenne et écart-type pour 100 dés ||",end="\n\n")
# Init des variables
l = []
n= 0
# Simulation des lancées de dé
for i in range(100):
    d = random.randint(1,6)
    l.append(d)
    n += d
# Calcul de la moyenne 
m = n/100
# Calcul de l'écart type
s = 0
for i in range(100):
    s += ((l[i]-m)**2)
s = (s/n)**0.5
# Résultats
print("Moyenne : {}".format(m))
print("Ecart-type : {}".format(s))
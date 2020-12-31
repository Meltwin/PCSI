import random
import pylab
print("\n|| Histogramme de n lancées de 1 dé, 2 dés, m dés ||",end="\n\n")
module = int(input("Quel module voulez-vous activer ?\n     1 -> 1 dé\n     2 -> 2 dés\n     3-> m dés\nModule "))
# Init des variables
n = int(input("Nombre de lancées : "))
if (module == 3):
    m = int(input("Nombre de dés par lancée : "))
l = []
if (module == 1):
    # Simulation des lancées de 1 dé
    for i in range(n):
        dA = random.randint(1,6)
        l.append(dA)
    pylab.hist(l,bins=6)
    pylab.show()
elif (module == 2):
    # Simulation des lancées de 2 dé
    for i in range(n):
        d = 0
        for j in range(2):
            d += random.randint(1,6)
        l.append(d)
    pylab.hist(l,bins=12)
    pylab.show()
elif (module == 3):
    # Simulation des lancées de m dé
    for i in range(n):
        d = 0
        for j in range(m):
            d += random.randint(1,6*m)
        l.append(d)
    pylab.hist(l,bins=6*m)
    pylab.show()

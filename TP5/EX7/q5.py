print('\n|| Construit {k≡0[7] ou (k≡0[3] et k≡0[4]) k∈⟦1,1000⟧} ||',end="\n\n")
# Init
l = []
# Parcours de tous les nombres entre 1 et 1000
for i in range(1,1001):
    # SI respectent les conditions
    if (i%7 == 0) or (i%3 == 0 and i%4 == 0):
        l.append(i)
# Résultats
print(l)
print("Nb de nombre = {}".format(len(l)))
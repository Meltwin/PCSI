# somme : fait la somme des éléments du tableau
# Arg : un tableau t
# Retourne : un réel somme(i = 0,len(t), t[i])
def somme(t):
    s = 0
    for i in range(len(t)):
        s += t[i]
    return s
# moyenne : sonne la moyenne des éléments du tableau
# Arg : un tableau t
# Retourne : un réel somme(i = 0,len(t), t[i])/len(t)
def moyenne(t):
    return somme(t)/len(t)
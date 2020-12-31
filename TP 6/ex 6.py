# min : return la valeur minimale
# Arg : un tableau t
# Retourne : un entier valeur min des éléments de t
def min(t):
    min = t[0]
    for i in range(1,len(t)):
        if (t[i] <min):
            min = t[i]
    return min
# argmin : return l'index de la valeur minimale
# Arg : un tableau t
# Retourne : entier la position de la valeur min des éléments de t
def argmin(t):
    min = t[0]
    pos = 0
    for i in range(1,len(t)):
        if (t[i] <min):
            min = t[i]
            pos = i
    return pos

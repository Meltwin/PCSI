# tri_croissant : retourne si le tableau est trié ou non
# Arg : un tableau t
# Retourne : un bool : True si trié, False si non trié
def tri_croissant(t):
    b = True
    for i in range(1,len(t)):
        if not(t[i-1] <= t[i]):
            b=False
    return b

print("\n|| Construit ⟦x,y⟧ ||",end="\n\n")
# Initialisation
x = int(input("x : "))
y = int(input("y : "))
# On met y le plus grand et x le plus petit
if (x>y):
    c = x
    x = y
    y = c
# On initialise la liste
l = [i for i in range(x,y+1)]
# Résultats
print(l)

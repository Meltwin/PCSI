print("\n|| Détermine si la liste est un mot de Lukasiewicz ||",end="\n\n")

# Init
l = [1,1,1,-1,1,-1,-1,-1,-1]
s = 0 # Somme des éléments
b = True # Variable d'état
# On parcours les éléments
for i in range(0,len(l)):
    s += l[i]
    # Si ne respecte pas la condition, on arrête tout
    if (i < len(l)-2 and not(s>=0)):
        print(i)
        b = False
# Résultat et condition finale somme == -1
if (b and s == -1):
    print("Mot de Lukasiewicz")
else:
    print("Pas un mot de Lukasiewicz")
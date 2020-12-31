import copy
print("\n|| Détermine si la liste est un mot de Lukasiewicz (par décapsulage) ||",end="\n\n")
# Init
l = [1,1,1,-1,1,-1,-1,-1,-1,-1]
capsule = [1,-1,-1]
sortie = []
first = True
while (l != sortie):
    if (first):
        first = False
    else:
        l = sortie
    sortie = []
    occ = 0
    # On parcours l
    for i in range(len(l)):
        if (occ != 0):
            occ -= 1 
        # Si encore possible
        if(i<len(l)-2):
            # Si respecte la condition du motif
            if (l[i]==capsule[0] and l[i+1]==capsule[1] and l[i+2]==capsule[2]):
                sortie.append(-1)
                occ = 3
            else:
                if (occ == 0):
                    sortie.append(l[i])
        # Sinon on remet les derniers caractères
        else:
            if (occ == 0):
                sortie.append(l[i])
# Résultat
if (sortie == [-1]):
    print("Mot de Lukasiewicz")
else:
    print("Pas un mot de Lukasiewicz")
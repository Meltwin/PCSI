print("\n|| Remplace les séquences [1,-1,-1] par [-1] ||",end="\n\n")
# Init
l = [1,1,1,-1,1,-1,-1,-1,-1]
capsule = [1,-1,-1]
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
print(sortie)
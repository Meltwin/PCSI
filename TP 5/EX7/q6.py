import random
print('\n|| Construit A×B ||',end="\n\n")
# Création des listes
a = [random.randint(0,1000) for i in range(random.randint(20,100))]
b = [random.randint(0,1000) for i in range(random.randint(20,100))]
# Init Ensemble AxB
produit_cartesien = []
# Calcul AxB
for i in range(len(a)):
    for j in range(len(b)):
        produit_cartesien.append([a[i],b[j]])
# Résultats
print(produit_cartesien)
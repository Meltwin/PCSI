print('\n|| Construit A⋃B ||',end="\n\n")
##### Initialisation des variables
a = [random.randint(0,1000) for i in range(random.randint(20,100))]
b = [random.randint(0,1000) for i in range(random.randint(20,100))]
# Calcul de l'union
union = list(set(a + b))
# Résultat
print(union)
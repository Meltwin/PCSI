print('\n|| Construit A⋂B ||',end="\n\n")

##### Initialisation des variables
a = [random.randint(0,1000) for i in range(random.randint(20,100))]
b = [random.randint(0,1000) for i in range(random.randint(20,100))]
inter = []
# On compare chaque élément de a et de b
for i in range(len(a)):
    for j in range(len(b)):
        # Si dans a et b
        if (a[i] == b[j]):
            inter.append(a[i])
inter = list(set(inter))
# Résultats
print(inter)
print('\n|| Construit {k*n, n∈ℕ, x<k*n<y} ||',end="\n\n")

# Initialisation des variables
x = int(input("x : "))
y = int(input("y : "))
k = int(input("k : "))
multiple = []
n = 0 # Compteur

# On met y le plus grand et x le plus petit
if (x>y):
    c = x
    x = y
    y = c

# On ajoute tous les multiples tant que multiple < y 
while (k*n<y):
    n += 1
    # Si multiple > x
    if (k*n>=x):
        multiple.append(k*n)
# Résultats
print(multiple)
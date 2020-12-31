# carre : affiche un carré de "*" de côté n
# Arg : entier n
def carre(n):
    for i in range(n):
        for j in range(n):
            print("*",end="")
        print()
# pyramide : affiche une pyramide de "*" de hauteur n
# Arg : entier n
def pyramide(n):
    for i in range(1,n+1):
        for j in range(i):
            print("*",end="")
        print()

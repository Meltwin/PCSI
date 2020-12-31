## Question 1 - Nb diviseurs
n = int(input("n = "))
nb = 0
if(n>1):
    for i in range(1,n+1):
        if (n%i == 0):
            nb +=1
    print(str(n)+" a "+str(nb)+" diviseurs")
else:
    print("La valeur n'est pas valide")

## Question 2 - Si premier
n = int(input("n = "))
nb = 0
if(n>1):
    for i in range(1,n+1):
        if (n%i == 0):
            nb +=1
    if (nb == 2):
        print("Ce nombre est premier")
    else:
        print("Ce nombre n'est pas premier")
else:
    print("La valeur n'est pas valide")

## Question 3 - Tous les premiers < M
m = int(input("m = "))
if(m>1):
    for u in range(1,m+1):
        nb = 0
        for i in range(1,u+1):
            if (u%i == 0):
                nb +=1
        if (nb == 2):
            print(str(u)+" est premier")
else:
    print("La valeur n'est pas valide")

## Question 4 - Nb nombre premier <= M
m = int(input("m = "))
nPremier = 0
if(m>1):
    for u in range(1,m+1):
        nb = 0
        for i in range(1,u+1):
            if (u%i == 0):
                nb +=1
        if (nb == 2):
            nPremier += 1
    print("Il y a "+str(nPremier)+" nombres premiers avant ou égal à m")
else:
    print("La valeur n'est pas valide")
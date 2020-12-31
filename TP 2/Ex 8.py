## User cherche

import random

coupM = int(input("Nombre max de coups : "))
a = random.randint(0,1000)
n = int(input("Quel prix ? "))
while (n != a):
    coupM -= 1
    if (n>a):
        print("C'est moins !")
    else:
        print("C'est plus !")
    print()
    if(coupM == 0):
        print("Vous avez perdu !")
        break
    n = int(input("Quel prix ? "))
if (coupM != 0):
    print("C'est trouvé ! ")
    
## ordi cherche
import random
import math

coupM = int(input("Nombre max de coups : "))
a = int(input("Le nombre que l'ordinateur doit trouver : "))

M = 1000
m = 0
n = 500
while (n != a):
    coupM -= 1
    print("L'ordinateur choisi "+str(n))
    if (n>a):
        print("C'est moins !")
        M = n
        n += math.floor((m-n)/2)
    else:
        print("C'est plus !")
        m = n
        n += math.floor((M-n)/2)
    print()
    if(coupM == 0):
        print("L'ordinateur a perdu !")
        break
if (coupM != 0):
    print("L'ordinateur choisi "+str(n))
    print("L'ordinateur a trouvé ! ")
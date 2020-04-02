import math
## Question 1
print("Veuillez rentrer h>a>b")
h = float(input("h = "))
a = float(input("a = "))
b = float(input("b = "))

if ((h**2) ==(a**2) + (b**2)):
    print("Triangle rectangle avec h comme hypothénuse")
else:
    print("Le triangle n'est pas rectangle")
    
"""
Test 3 4 5 : le triangle est rectangle
Test 3 5 7 : le triangle n'est pas rectangle

pour 0.03 0.04 0.05 cela ne marche pas
"""

## Question 3 - Version corrigée
print("Veuillez rentrer h>a>b")
h = float(input("h = "))
a = float(input("a = "))
b = float(input("b = "))
print()
e = float(input("ε = "))
print()

def acceptable(a,b):
    import math
    global e
    if (math.fabs(a-b) < e):
        return True
    else:
        return False

if (acceptable((h**2),(a**2) + (b**2))):
    print("Triangle rectangle avec h comme hypothénuse")
else:
    print("Le triangle n'est pas rectangle")
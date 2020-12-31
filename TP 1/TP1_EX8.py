## Exercice 8 - 1
annee = int(input("Année : "))

def mod(a,d):
    return (a%d)==0

if (mod(annee,400)):
    print("Bisextile")
else:
    if (mod(annee,4)):
        if (mod(annee,100)):
            print("Non Bisextile")
        else :
            print("Bisextile")
    else:
        print("Non Bisextile")
        
        
## Exercice 8 - 2
annee = int(input("Année : "))

def mod(a,d):
    return (a%d)==0
     
print(mod(annee,400) or (mod(annee,4) and not(mod(annee,100))))
## Question 1
import time
jours = [0,31,28,31,30,31,30,31,31,30,31,30,31]
jour = int(input("Jour : "))
mois = int(input("Mois : "))
annee = int(input("Année : "))

def nbSInDay():
    return 3600*24
def nbSInMonth(m):
    return nbSInDay()*jours[m]
def nbSInYear():
    s = 0
    for i in range(1,13):
        s += nbSInMonth(i)
    return s

seconds = 0
for k in range(1970, annee):
    seconds += nbSInYear()
for k in range(1,mois):
    seconds += nbSInMonth(k)
for k in range(1,jour):
    seconds += nbSInDay()
print(seconds)
## Question 2 - between 2 dates
import math
jours = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def nbSInDay():
    return 3600*24
def nbSInMonth(m):
    return nbSInDay()*jours[m]
def nbSInYear():
    s = 0
    for i in range(1,13):
        s += nbSInMonth(i)
    return s
def  getNbDay(seconds):
    return seconds//nbSInDay()

def getSecondFromDate(annee,mois,jour):
    seconds = 0
    for k in range(1970, annee):
        seconds += nbSInYear()
    for k in range(1,mois):
        seconds += nbSInMonth(k)
    for k in range(1,jour):
        seconds += nbSInDay()
    return seconds
    
jourA = int(input("Jour : "))
moisA = int(input("Mois : "))
anneeA = int(input("Année : "))
jourB = int(input("Jour : "))
moisB = int(input("Mois : "))
anneeB = int(input("Année : "))
print(int(math.fabs(getNbDay(getSecondFromDate(anneeB,moisB,jourB)-getSecondFromDate(anneeA,moisA,jourA)))))


## Question 3
import time
jours = [0,31,28,31,30,31,30,31,31,30,31,30,31]
joursB = [0,31,29,31,30,31,30,31,31,30,31,30,31]
jour = int(input("Jour : "))
mois = int(input("Mois : "))
annee = int(input("Année : "))
def isBisextile(y):
    return (y%400 == 0 or (y%4 == 0 and y%100 !=0))
def nbSInDay():
    return 3600*24
def nbSInMonth(m,b):
    if (b):
        return nbSInDay()*joursB[m]
    else:
        return nbSInDay()*jours[m]
def nbSInYear(y):
    if (isBisextile(y)):
        s = 0
        for i in range(1,13):
            s += nbSInMonth(i,True)
        return s
    else:
        s = 0
        for i in range(1,13):
            s += nbSInMonth(i,False)
        return s

seconds = 0
for k in range(1970, annee):
    seconds += nbSInYear(k)
for k in range(1,mois):
    if (isBisextile(annee)):
        seconds += nbSInMonth(k,True)
    else:
        seconds += nbSInMonth(k,False)
for k in range(1,jour):
    seconds += nbSInDay()
print(seconds)

## Question 4
import time
jours = [0,31,28,31,30,31,30,31,31,30,31,30,31]
joursB = [0,31,29,31,30,31,30,31,31,30,31,30,31]
jour = int(input("Jour : "))
mois = int(input("Mois : "))
annee = int(input("Année : "))

def isBisextile(y):
    return (y%400 == 0 or (y%4 == 0 and y%100 !=0))
def nbSInDay():
    return 3600*24
def nbSInMonth(m,b):
    if (b):
        return nbSInDay()*joursB[m]
    else:
        return nbSInDay()*jours[m]
def nbSInYear(y):
    if (isBisextile(y)):
        s = 0
        for i in range(1,13):
            s += nbSInMonth(i,True)
        return s
    else:
        s = 0
        for i in range(1,13):
            s += nbSInMonth(i,False)
        return s
def getNbDay(s):
    return s//nbSInDay()
def getSecondFromDate(annee,mois,jour):
    seconds = 0
    for k in range(1970, annee):
        seconds += nbSInYear(k)
    for k in range(1,mois):
        if (isBisextile(annee)):
            seconds += nbSInMonth(k,True)
        else:
            seconds += nbSInMonth(k,False)
    for k in range(1,jour):
        seconds += nbSInDay()
    return seconds
j = int(getNbDay(getSecondFromDate(annee,mois,jour))%7)

if (j == 0):
    print("Jeudi")
elif (j==1):
    print("Vendredi")
elif(j==2):
    print("Samedi")
elif (j==3):
    print("Dimanche")
elif (j==4):
    print("Lundi")
elif (j==5):
    print("Mardi")
elif (j==6):
    print("Mercredi")
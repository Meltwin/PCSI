## Exercice 7
a = int(input("a :"))
b = int(input("b :"))
c = int(input("c :"))

m = 0
if (a>=b):
    if (a>=c):
        m = a
    else:
        m = c
else:
    if(b>=c):
        m=b
    else:
        m=c
        
print("m = "+str(m))

## Exercice 7 - Modifié
a = int(input("a :"))
b = int(input("b :"))
c = int(input("c :"))
print()

def blocBC(b,c):
    if (b>=c):
        prt("b")
        print("c")
    else:
        prt("c")
        print("b")
        
def blocAC(a,c):
    if (a>=c):
        prt("a")
        print("c")
    else:
        prt("c")
        print("a")
        

def prt(s):
    print(s+" >= ",end="")

if (a>=b):
    if (a>=c):
        prt("a")
        blocBC(b,c)
    else:
        prt("c")
        prt("a")
        print("b")
else:
    if(b>=c):
        prt("b")
        blocAC(a,c)
    else:
        prt("c")
        prt("b")
        print("a")
        
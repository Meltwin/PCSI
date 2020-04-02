 ## [Exercice 4]
 
a = int(input("a :"))
b = int(input("b :"))
c = int(input("c :"))

a = a+b+c
b = b+c
c = b-c
b = a-b
a = a-b-c

print("a = "+str(a))
print("b = "+str(b))
print("c = "+str(c))

## [Exercice 4] Réécriture du programme

a = int(input("a :"))
b = int(input("b :"))
c = int(input("c :"))

d =a
a = c
c = b
b = d

print("a = "+str(a))
print("b = "+str(b))
print("c = "+str(c))

## [Exercice 4] A quatre variablesa = int(input("a :"))
a = int(input("a :"))
b = int(input("b :"))
c = int(input("c :"))
d = int(input("c :"))

a = a+b+c+d
b = b+c+d
c = c+d
d = c-d
c = b-c
b = a-b
a=a-b-c-d

print("a = "+str(a))
print("b = "+str(b))
print("c = "+str(c))
print("d = "+str(d))
## Formule de Héron
import math
a = int(input("a :"))
b = int(input("b :"))
c = int(input("c :"))

p = (a+b+c)/2
a = math.sqrt(p*float(p-a)*float(p-b)*float(p-c))

print("Périmètre = "+str(p*2))
print("Aire = "+str(a))
import numpy as np
t = np.array([15,3,9,1,64,12,7,3,16,10,3,2,18,1,21])
## If val is in array
x = int(input("Valeur : "))
b = False
for i in range(len(t)):
    if x == t[i]:
        print("True")
        b = True
if not(b):
    print("False")
## Number of occurence
x = int(input("Valeur : "))
b = 0
for i in range(len(t)):
    if x == t[i]:
        b +=1
print("Nombre d'occurence = {}".format(b))
## Number of occurence
x = int(input("Valeur : "))
b = 0
for i in range(len(t)):
    if x == t[i]:
        print(i)
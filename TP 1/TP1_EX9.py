 ## Exercice 9 - 1
n = int(input("N :"))

for i in range(n+1):
    for j in range(n+1):
        print(str(i)+"x"+str(j)+" = "+str(i*j)) 
        
## Exercice 9 - 2
n = int(input("N :"))
print()

b=0
for i in range(n+1):
    for j in range(n+1):
        print(str(i)+"x"+str(j)+" = ",end="")
        
        r = int(input())
        if (r != (i*j)):
            b+=1
print("Erreurs :"+str(b))
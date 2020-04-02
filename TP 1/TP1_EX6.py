## Programme de base
n = int(input("n : "))

while n!=1:
    if (n%2)==0:
        n = int(n/2)
    else:
        n = int(n/3)+1.0
        
## Programme modifié
n = int(input("n : "))

t = 0
while n!=1:
    if (n%2)==0:
        n = int(n/2)
    else:
        n = int(n/3) + 1
    t = t+1
print(t)
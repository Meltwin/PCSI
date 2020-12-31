## Question 1 - Calcul de u(n)
n = int(input("N = "))
u = 0
v = 1
if (n <2):
    print("L'entier entré est trop petit")
else:
    for i in range(2,n+1):
        w = u + v
        u = v
        v = w
    print(v)
    
## Question 2 - Calcul de tous les u(n) jusqu'a n
n = int(input("N = "))
u = 0
v = 1
if (n <2):
    print("L'entier entré est trop petit")
else:
    print("U0 = "+str(u))
    print("U1 = "+str(v))
    for i in range(2,n+1):
        w = u + v
        u = v
        v = w
        print("U"+str(i)+" = "+str(v))
        
"""
La suite de fibonacci semble tendre vers + infini quand n tend vers + infini
"""

## Question 3 - rapport entre u(n+1) et u(n)
n = int(input("N = "))
u = 0
v = 1
if (n <2):
    print("L'entier entré est trop petit")
else:
    print("U0 = "+str(u))
    print("U1 = "+str(v))
    for i in range(2,n+1):
        w = u + v
        u = v
        v = w
        print("K = "+str(i)+", Diff = "+str(v/u))
        
""" 
On constate que le rapport tend vers 1.618033988749895, c'est le nombre d'or
"""
### Question 4 - u(k) / v(k)
n = int(input("N = "))
u = 0
z = 1
if (n <2):
    print("L'entier entré est trop petit")
else:
    print("U0 = "+str(u))
    print("U1 = "+str(v))
    for i in range(2,n+1):
        w = u + z
        u = v
        z = w
        v = (5**(-0.5))*(((1+math.sqrt(5))/2)**i)
        print("K = "+str(i)+", u(k) / v(k) = "+str(z/v))
        
"""
Quand n -> + infini, le rapport entre u(n) et v(n) tend vers 1
Donc en + infini, la valeur de v(n) est quasiment la même que celle de u(n)
Donc en + infini, la suite v(n) se comporte pratiquement comme la suite u(n)
"""
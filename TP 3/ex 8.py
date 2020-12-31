b = False
n = 10

def getPowerTen(nb):
    k = 0
    while(nb>=10):
        k +=1
        nb = nb//10
    return k
def getRotated(n):
    firstDigit = n//(10**getPowerTen(n))
    p = (n%(10**getPowerTen(n)))*10 + firstDigit
    return p
  
while not(b):
    n +=1
    
    # Nombre permuté
    p = getRotated(n)
    #print("N : {}, P : {}".format(n,p))
    
    #print(int(n*3/2))
    
    if ((n*3)//2 == p):
        print("N = {}".format(n))
        b = True
##  Retry
b =False

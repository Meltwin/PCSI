import math
b = False
N = 1
while (not(b)):
    s = 0
    for k in range(1,N):
        s += math.exp(k)
    print("Somme {} = {}".format(N,s))
    if (s > 1000):
        b =True
    N +=1
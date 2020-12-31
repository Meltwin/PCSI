import math

nGrain = 0
k = 0
while nGrain <=12345:
    k = k+1
    d = k
    while d>=1000:
        d = d//10
        if (d%1000 == 666):
            nGrain += 1
            break
print(k)
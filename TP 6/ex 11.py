# fibo : affiche le n-ème nombre de la suite de fibonacci
# Arg : entier n
def fibo(n):
    u = 0
    v = 1
    for i in range(2,n+1):
        w = u + v
        u = v
        v = w
    print(v)
fibo(4)
def fn(x,n):
    return (x**n -n*x -1)
n = int(input("n : "))
eps = float(input("eps : "))
def dicho(eps, a0,b0,n):
    a = a0
    b = b0
    while (b-a)>eps:
        m = (a+b)/2
        if (fn(a,n)*fn(m,n)<0):
            b = m
        else:
            a = m
    return (b+a)/2
print(dicho(eps,1,3,n))
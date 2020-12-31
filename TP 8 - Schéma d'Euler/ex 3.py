def radiocarbone(c0,lambd,h,t):
    a = [0]
    c = [c0]
    k = 0
    while a[k]<t:
        k+=1
        a.append(a[k-1] + h)
        c.append(c[k-1] + h*(-lambd*c[k-1]))
    return c[-1]
r = radiocarbone(1E-12,1.210*1E-4,1,1)
print(r)
r = radiocarbone(1E-12,1.210*1E-4,1,2)
print(r)
r = radiocarbone(1E-12,1.210*1E-4,1,3)
print(r)
r = radiocarbone(1E-12,1.210*1E-4,1,10)
print(r)
r = radiocarbone(1E-12,1.210*1E-4,1,20)
print(r)
r = radiocarbone(1E-12,1.210*1E-4,1,50)
print(r)

## Q3
def datation(c0,lam,c):
    tau = 1/lam
    h = 0.1*tau
    a = [0]
    y = [c0]
    k = 0
    while y[k]>c:
        k+=1
        a.append(a[k-1] + h)
        y.append(y[k-1] + h*(-lam*y[k-1]))
    return k
n = datation(1E-12,1.210*1E-4,0.7*1E-12)
print(n)
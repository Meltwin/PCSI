t = []
def calced(x):
    global t
    for i in t:
        if i[0] == x[0]:
            if i[1] == x[1]:
                if i[2] == x[2]:
                    return True
                else :
                    return False
            elif i[1] == x[2]:
                if i[2] == x[1]:
                    return True
                else:
                    return False
            else:
                return False
        elif i[0] == x[1]:
            if i[1] == x[0]:
                if i[2] == x[2]:
                    return True
                else:
                    return False
            elif i[1] == x[2]:
                if i[2] == x[0]:
                    return True
                else:
                    return False
            else:
                return False
        elif i[0] == x[2]:
            if i[1] == x[0]:
                if i[2] == x[1]:
                    return True
                else:
                    return False
            elif i[1] == x[1]:
                if i[1] == x[0]:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False


m = int(input("Max : "))
b = False
for i in range(1, m+1):

    for j in range(1,m+1):
        for k in range(1,m+1):
            if (i**2)==((j**2)+(k**2)):
                if not(calced([j,i,k])):
                    print(str(k)+" | "+str(j)+" | "+str(i))
                    t.append([j,i,k])
                    b = True
    if(b):
        print()
        b = False
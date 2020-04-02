for c in range(100):
    for b in range(c+1):
        for a in range(b+1):
            if(a*b*c == 36):
                s = a+b+c
                print("Le triplet {}, {}, {} avec comme somme : {}".format(a,b,c,s))
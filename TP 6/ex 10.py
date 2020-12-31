# table : affiche la table de multiplication de n
# Arg : entier n
def table(n):
    for i in range(11):
        print("{0}x{1}={2}".format(i,n,i*n))
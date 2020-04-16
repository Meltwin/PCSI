import numpy as np
import matplotlib.pyplot as plt
def lagrange(x,i,a):
    Li = 1
    for j in range(len(a)):
        if (i != j):
            Li *= (x-a[j])/(a[i]-a[j])
    return Li
def interpol(x,a,b):
    P = 0
    for i in range(len(a)):
        P += b[i]*lagrange(x,i,a)
    return P
def interpol_fichier(fichier):
    # Open file
    f = open(fichier,'r')
    lignes = f.readlines()
    f.close()

    # Add points to array a & b
    a = np.zeros(len(lignes))
    b = np.zeros(len(lignes))
    for i in range(len(lignes)):
        t = lignes[i].split()
        a[i] = t[0]
        b[i] = t[1]
    
    # Show the fixing points
    plt.scatter(a,b)

    # Create the linspace
    abcisse = np.linspace(min(a)-0.5,max(a)+0.5,10000)
    ordonne = [interpol(k,a,b) for k in abcisse]
    plt.plot(abcisse,ordonne)
    plt.show()
interpol_fichier("D:/Dev/Python/PCSI/TP 13/interpolation.txt")
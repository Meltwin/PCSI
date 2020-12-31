import numpy as np
import numpy.linalg as nlg
## EX 1
A = np.array([[1,0,-1],[2,-1,0]])
B = np.array([[1,0,0],[1,-1,0],[0,1,0]])
C = np.array([[2,-1,1],[0,0,-3],[2,1,1]])
D = np.array([[1,2,3]])
E = np.array([[1],[2],[3]])
F = np.array([[1,1],[1,1]])
## EX 2
print(A+A)
print(2*A)
print(2*B-3*C)
print(A@B)
print(A@B + A)
#print(A+B) Pas la même taille
#print(np.transpose(A)) Pas carré
print(B+C)
print(np.linalg.matrix_power((B+C),10))
#print(B@A) Nb colonne B != Nb ligne A
#print((np.transpose(B))@A) Nb colonne t(B) != Nb ligne A
#print(np.linalg.inv(B)) Non inversible
print(np.linalg.inv(C))

## EX 3
M = np.array([[-4,5,1,2,0],[-1,2,0,4,2],[0,5,-1,-2,1],[1,2,3,8,-1],[-2,-6,1,2,0]])

# Calcul Q2
R = nlg.matrix_power(M,5)-5*nlg.matrix_power(M,4)-16*nlg.matrix_power(M,3)-146*nlg.matrix_power(M,2)-929*M
print(R)

# Q3 
"""
On obtient R = -290*I5
En factorisant par M on obtient
    M(M^4 - 5M^3 - 16M^2 - 146*M -929*I5) = -290*I5
    Donc M est inversible d'inverse (M^4 - 5M^3 - 16M^2 - 146*M -929*I5)/-290
"""
#Q4
Inverse = (nlg.matrix_power(M,4) - 5*nlg.matrix_power(M,3) - 16*nlg.matrix_power(M,2) - 146*M -929*np.eye(5))/-290
print("Inverse :")
print(Inverse)
print(nlg.inv(M))
print(Inverse-nlg.inv(M))
## EX 4
notes = np.array([12,8,15,7,6,15,17,10])
coeffs = np.array([1,1,3,2,2,5,3,1])

notesApp = notes*coeffs
tot = np.sum(notesApp)
totCoeff = np.sum(coeffs)
moy = tot/(totCoeff)
print(moy)
## Ex 5

G = np.block([[D],[A]])
print(G)
H = np.block([[D],[D],[D]])
print(H)
J = np.block([[E,E,E]])
print(J)
K = np.block([[F,F],[F,F]])
print(K)
## EX 6
M = np.array([[-4,5,1,2,0],[-1,2,0,4,2],[0,5,-1,-2,1],[1,2,3,8,-1],[-2,-6,1,2,0]])
print(M[0,0]+M[1,1]+M[2,2])
M[2,4] = 999
print(M)
## EX 7
M = np.array([[3,2,1],[2,3,1],[3,1,0]])

L1 = M[0,:]
print(L1)

C3 = M[:,2]
print(C3)

M[0,:] = np.array([1,1,1])
print(M)

M[1,:] = M[1,:]-2*M[0,:]
print(M)

M[2,:] = M[2,:] - 3*M[0,:]
M[2,:] = (-1/2)*M[2,:]
M[2,:] = M[2,:] - M[1,:]
M[2,:] = M[2,:]/2
M[1,:] = M[1,:] + M[2,:]
M[0,:] -= M[2,:]
M[0,:] -= M[1,:] # On a l'échelonnée réduite
print(M)
## EX 8
A = np.zeros([10,10])
for i in range(1,11):
    for j in range(1,11):
        A[i-1,j-1] = 2*i+j+1
print(A)
## EX 9
A = np.array([[2,3,-5],[-1,1,1],[2,-1,2]])
B = np.array([[0],[1],[2]])

print(nlg.solve(A,B))

#
A = np.array([[1,-1,1],[-1,2,-2],[0,1,1]])
B =np.array([[3],[-5],[2]])
print(nlg.solve(A,B))

#
A = np.array([[2,1,-1],[1,0,1],[0,0,1]])
B =np.array([[2],[2],[10]])
print(nlg.solve(A,B))

#
A = np.array([[3,2],[2,-1]])
B =np.array([[4],[2]])

R = nlg.solve(A,B)
print(R[0,0]+R[1,0])
print(R)
"""
Numérique il n'y a pas de solution
"""
## EX 10

# trace : retourne la trace d'une matrice
# Arg : np.array[][] M, une matrice
# Retour : int t, la trace de M
def trace(M):
    t = 0
    n,m = np.shape(M)
    for i in range(n):
        t += M[i,i]
    return t
m = np.array([[1,0,0],[0,1,0],[0,0,1]])
print(trace(m))

## EX 11
import matplotlib.pyplot as plt
# fibo : retourne le n-ième terme de la suite de fibonacci
#Arg : int n, le rang
# Retour : int u, la valeur 
def fibo(n):
    m = np.array([[1,1],[1,0]])
    F = nlg.matrix_power(m,n)
    return F[0,1]

n=20
pts = [fibo(k) for k in range(n+1)]
abs = [k for k in range(n+1)]
plt.plot(abs,pts)
plt.show()

## EX 12
# recherche : retourne si la valeur x est dans la matrice x
# arg : np.array[][] M la matrice, float x le nombre
# retour : bool b, le résultat de la recherche
def recherche(M,x):
    n,m = np.shape(M)
    b = False
    for i in range(n):
        for j in range(m):
            if (M[i,j] == x):
                b = True
    return b
# minmat : retourne le plus petit coeff de la matrice
# arg : np.array[][] M la matrice
# retour : int mi le minimum de la matrice
def minmat(M):
    n,m = np.shape(M)
    mi = M[0,0]
    for i in range(n):
        for j in range(m):
            if (M[i,j] < mi):
                mi = M[i,j]
    return mi
# posmaxmat : retourne la position du plus gros coeff de la matrice
# arg : np.array[][] M la matrice
# retour : int[2] pos 
def posmaxmat(M):
    n,m = np.shape(M)
    mi = M[0,0]
    pos = [0,0]
    for i in range(n):
        for j in range(m):
            if (M[i,j] > mi):
                mi = M[i,j]
                pos = [i,j]
    return pos

M = np.array([[0,18,9],[19,522,87],[69,87,2]])
print(recherche(M,522))
print(minmat(M))
print(posmaxmat(M))
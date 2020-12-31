## Question 1
CA = float(input("[A] = "))
CB = float(input("[B] = "))
CC = float(input("[C] = "))
Ke = float(input("Ke = "))

Q = (CC**2)/((CA**2)*CB)
if (Q > Ke):
    print("La réaction va se poursuivre dans le sens indirect")
else:
    print("La réaction va se poursuivre dans le direct")
    
## Question 2 - Modifié
CA = float(input("[A] = "))
CB = float(input("[B] = "))
CC = float(input("[C] = "))
Ke = float(input("Ke = "))

Q = (CC**2)/((CA**2)*CB)
if (Q > Ke):
    print("La réaction va se poursuivre dans le sens indirect")
elif (Q == ke):
    print("La réaction est équilibrée")
else:
    print("La réaction va se poursuivre dans le sens direct")
    
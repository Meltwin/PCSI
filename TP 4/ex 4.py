import numpy as np
t = np.array([15,3,9,1,64,12,7,3,16,10,3,2,18,1,21,19,15,11,9])
## Is sorted ?
b = True
for i in range(1,len(t)):
    if not(t[i]>=t[i-1]):
        b=False
print(b)
## Max consecutive decroissant val
t = np.array([15,3,9,1,64,12,7,3,16,10,3,2,18,1,21,19,15,11,9])
tempStart = 0
tempEnd = 0
finalStart = 0
finalEnd = 0
for i in range(1,len(t)):
    if t[i]<t[i-1]:
        tempEnd = i
    else:
        if ((tempEnd-tempStart) >(finalEnd-finalStart)):
            finalStart = tempStart
            finalEnd = tempEnd
        tempStart = i
        tempEnd = i
if ((tempEnd-tempStart) >(finalEnd-finalStart)):
    finalStart = tempStart
    finalEnd = tempEnd
print("La suite de case démarre de {0} et s'arrête à {1}".format(finalStart,finalEnd))
print("Le contenu est : ")
for i in range(finalStart,finalEnd+1):
    print(t[i],end=" ")
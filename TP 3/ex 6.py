
## Question 1
n = input("N = ")
s = 0
for i in range(len(n)):
    s += int(n[i])
print(s)
## Question 2
import math
n = input("N = ")
s = 0
for i in range(len(n)):
    s += int(n[i])
k = 0
b = False
while (k <=math.ceil(s/3) and not(b)):
    if (3**k == s):
        b = True
    k += 1
if (b):
    print("Divisible par 3")
else:
    print("Non divisible par 3")
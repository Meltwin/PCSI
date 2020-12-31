import numpy as np
import matplotlib.pyplot as plt
## 1 - Calc n ieme terme de la suite
n = int(input("n = "))
t = np.zeros(n+1)
t[0] = 1
for i in range(1,n+1):
    t[i] = 1 + 1/t[i-1]
print(t[len(t)-1])
## Show table
import numpy as np
import matplotlib.pyplot as plt
n = int(input("n = "))
t = np.zeros(n+1)
t[0] = 1
for i in range(1,n+1):
    t[i] = 1 + 1/t[i-1]
plt.plot(t)
plt.show()
## With v 
import numpy as np
import matplotlib.pyplot as plt
import math
def VN(u):
    return math.log10(math.fabs(u-(1+(5**0.5))/2))
n = int(input("n = "))
t = np.zeros(n+1)
v = np.zeros(n+1)
t[0] = 1
v[0] = VN(t[0])
for i in range(1,n+1):
    t[i] = 1 + 1/t[i-1]
    v[i] = VN(t[i])
plt.plot(t)
plt.plot(v)
plt.show()
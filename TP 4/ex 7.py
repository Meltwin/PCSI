## Fibonnaci
import numpy as np
import matplotlib.pyplot as plt
n = int(input("n = "))
t = np.zeros(n+1)
t[0] = 0
t[1] = 1
for i in range(2,n+1):
    t[i] = t[i-1] + t[i-2]
plt.plot(t)
plt.show()
"""
La croissance a une allure exponentielle
"""
# f est continue sur [0,1] donc l'intégrale peut être définie sur [0,1]
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
def f(x):
    return (1-x**2)**0.5
ab = np.linspace(0,1)
o = [f(k) for k in ab]
plt.plot(ab,o)
plt.grid(True)
plt.show()
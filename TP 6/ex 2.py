## Q1
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,2*np.pi,100) # 100 pts
plt.plot(x,np.cos(x))
plt.show()
""" Affiche x->cos(x) sur [0,2pi]"""
## Q2
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,2*np.pi,100) # 100pts
plt.plot(x,np.cos(x),x,np.sin(x))
plt.legend(["cos","sin"])
plt.show()
## Q3
import matplotlib.pyplot as plt
import numpy as np
def f(x):
    return (1-x)*((1-x**2)**0.5)
x = np.linspace(-1,1,200)
plt.plot(x,f(x))
plt.show()
## Q4
import matplotlib.pyplot as plt
import numpy as np
# f
# Arg : réel x
# Retourne : un réel égal à (1-x)*sqrt(1-x**2)
def f(x):
    return (1-x)*((1-x**2)**0.5)
# g
# Arg : réel x
# Retourne : un réel x**3 / x**2 + 1
def g(x):
    return (x**3)/(x**2 +1)
# h
# Arg : réel x
# Retourne : un réel égal à f(x)-g(x)
def h(x):
    return f(x)-g(x)
x = np.linspace(-1,1,200)
plt.plot(x,f(x),x,g(x),x,h(x))
plt.legend(["f","g","h"])
plt.show()
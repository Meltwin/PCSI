import numpy as np
import matplotlib.pyplot as plt
# falpha 
# Arg : un flottant alpha (paramètre), un flottant (variable  réelle) t
# Retourne :  un réel -cos(t)+alpha*sin(t)
def f(alpha,t):
    return -np.cos(t)+alpha*np.sin(t)
    
x = np.linspace(0,np.pi,100)
plt.plot(x,f(-2,x),x,f(-1,x),x,f(0,x),x,f(1,x),x,f(2,x))
plt.legend(["-2","-1","0","1","2"])
plt.show()
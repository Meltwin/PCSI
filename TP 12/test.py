from scipy.integrate import quad 
from pylab import *

import numpy as np

xmin = 0.0
xmax = 9.0 * ( np.pi / 2.0 )

def function(x): 
    return np.cos(x)

res, err = quad(function, xmin, xmax) 
print('norm: ', res)

t = arange(xmin, xmax, 0.01)

ax = subplot(111)
ax.plot(t, function(t),'r-')

ax.grid(True)

ax.set_xlim(xmin,xmax)
ax.set_ylim(-1.25,1.25)

ax.fill_between(t, 0, function(t))

#plt.savefig('IntegraleSimplePython.png')
show()
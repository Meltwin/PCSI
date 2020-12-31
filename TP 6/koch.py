import numpy as np
import matplotlib.pyplot as plt
# posC :  retourne la pos du point C
# Arg : float[] abs, float[] ord
# Retourne : float[] [x,y]
def posC(abs,ord):
    pos = [0,0]
    pos[0] = (1/3)*(abs[1]-abs[0])
    pos[1] = (1/3)*(ord[1]-ord[0])
    return pos
# posD :  retourne la pos du point D
# Arg : float[] abs, float[] ord
# Retourne : float[] [x,y]
def posD(abs,ord):
    pos = [0,0]
    pos[0] = (2/3)*(abs[1]-abs[0])
    pos[1] = (2/3)*(ord[1]-ord[0])
    return pos
# posE :  retourne la pos du point E
# Arg : float[] abs, float[] ord
# Retourne : float[] [x,y]
def posE(abs,ord):
    pos = [0,0]
    pos[0] = (0.5*(abs[1]-abs[0])+(((3)**0.5)/2)*(ord[1]-ord[0]))/3 + (2/3)*abs[0] + (1/3)*abs[1]
    pos[1] = (0.5*(ord[1]-ord[0])+(((3)**0.5)/2)*(abs[1]-abs[0]))/3 + (2/3)*ord[0] + (1/3)*ord[1]
    return pos
    
    
# posNext :  retourne les pos des points du prochain rang du segment
# Arg : float[] abs, float[] ord
# Retourne : float[] abs, float[] ord
def pos(abs,ord):
    aOut = [abs[0]]
    oOut = [ord[0]]
    
    # Point C
    c = posC(abs,ord)
    aOut.append(c[0])
    oOut.append(c[1])
    
    # Point E
    e = posE(abs,ord)
    aOut.append(e[0])
    oOut.append(e[1])
    
    # Point D
    d = posD(abs,ord)
    aOut.append(d[0])
    oOut.append(d[1])
    
    aOut.append(abs[1])
    oOut.append(ord[1])
    return [aOut,oOut]

init = [[0,10,5,0],[0,0,5,0]]
def main(n):
    global init
    out = []
    for i in range(1,len(init[0])):
        out += pos([init[0][i-1],init[0][i]],[init[1][i-1],init[1][i]])
    init = out
    print(out)
main(1)
plt.plot(init[0],init[1])
plt.show()
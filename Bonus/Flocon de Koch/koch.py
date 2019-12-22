###########################################
#               Dependencies              #
###########################################
import numpy as np
import matplotlib.pyplot as plt
import copy as cp
import math

###########################################
#          Calculs des positions          #
###########################################

# posC :  retourne la position du point C
# Arg : float[] abs, float[] ord
# Retourne : float[] [x,y]
def posC(abs,ord):
    pos = [0,0]
    pos[0] = abs[0]+(1/3)*(abs[1]-abs[0])
    pos[1] = ord[0]+(1/3)*(ord[1]-ord[0])
    return pos
# posD :  retourne la position du point D
# Arg : float[] abs, float[] ord
# Retourne : float[] [x,y]
def posD(abs,ord):
    pos = [0,0]
    pos[0] = abs[0]+(2/3)*(abs[1]-abs[0])
    pos[1] = ord[0]+(2/3)*(ord[1]-ord[0])
    return pos
# posE :  retourne la pos du point E en faisant une rotation via exp(i*pi/3) = 60°
# Arg : float[] abs, float[] ord
# Retourne : float[] [x,y]
def posE(abs,ord):
    pos = [0,0]
    pos[0] = 0.5*(abs[1]-abs[0])-(((3)**0.5)/2)*(ord[1]-ord[0]) + abs[0] # Partie réelle
    pos[1] =0.5*(ord[1]-ord[0])+(((3)**0.5)/2)*(abs[1]-abs[0]) + ord[0] # Partie immaginaire
    return pos
    
# pos :  retourne les pos des points du segment rang +1
# Arg : float[] abs, float[] ord
# Retourne : float[] abs, float[] ord
def pos(abs,ord):
    # On rajoute le début du segment (déjà existant)
    aOut = [abs[0]]
    oOut = [ord[0]]
    
    # On créé et on ajoute le point C
    c = posC(abs,ord)
    aOut.append(c[0])
    oOut.append(c[1])

    # On créé le point D
    d = posD(abs,ord)
    
    # On créé le point E par rapport à C et D et on l'ajoute au segment
    e = posE([c[0],d[0]],[c[1],d[1]])
    aOut.append(e[0])
    oOut.append(e[1])
    
    # On ajoute le point D au segment
    aOut.append(d[0])
    oOut.append(d[1])
    
    # On rajoute la fin du segment (déjà existant)
    aOut.append(abs[1])
    oOut.append(ord[1])
    return [aOut,oOut]

###########################################
#               Main Program              #
###########################################

init = [[0,10,5,0],[0,0,-7.5,0]] # Segment de base
# Calcul pour une profondeur de plus
# Ici "init" est le tableau contenant les abcisses et ordonnées de tous les points de la figure entière du rang n-1
def main():
    global init
    out = [[],[]] # variable temporaire pour la profondeur
    for i in range(1,len(init[0])):
        tmp = cp.deepcopy(pos([init[0][i-1],init[0][i]],[init[1][i-1],init[1][i]]))
        # On sépare entre x et y
        out[0] += tmp[0]
        out[1] += tmp[1]
    init = out # On sauvegarde la figure calculée

# Pour n profondeur demandée
for _ in range(int(input("Profondeur : "))):
    main() # On calcule la nouvelle forme 

# Affichage
plt.fill(init[0],init[1]) # Figure remplie
plt.axis('equal') # On se place dans un repère orthonormé
plt.show()

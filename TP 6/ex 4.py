import numpy as np
# volumeCube : retourne le volume d'un cube
# Arg : flottant x
# Retourne : flottant x*x*x
def volumeCube(x):
    return x*x*x
# volumeTetra : retourne le volume d'un tétraèdre
# Arg : flottant x
# Retourne : flottant x**3 / (6*sqrt(2))
def volumeTetra(x):
    return (x**3) / (6*((2)**0.5))
# volumeBoule : retourne le volume d'une boule
# Arg : flottant d
# Retourne : flottant (pi*volumeCube(d))/6
def volumeBoule(d):
    return (np.pi*volumeCube(d))/6
    
x = float(input("x = "))
print("Volume du cube = {}".format(volumeCube(x)))
print("Volume du tétraèdre = {}".format(volumeTetra(x)))
print("Volume de la boule = {}".format(volumeBoule(x)))
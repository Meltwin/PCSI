from Snake.Game import *
from Snake.Serpent import *

#n = int(input("Nombre de joueur :"))
print("############## SNAKE ###############")
print("Max 4 personnes")
g = Game()
for _ in range(1,n+1):
    name = input("Entrer le nom du joueur {0} : ".format(_))
    s = Serpent(name)
    g.addPlayer(s)
g.init()
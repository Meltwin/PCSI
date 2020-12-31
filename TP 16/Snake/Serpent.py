#from Snake.Game import *
class Serpent:

    DIRECTION = ["droite","bas","gauche","haut"]
    MAX_HEALTH = 80
    APPLE_HEALTH = MAX_HEALTH

    TICK_PER_HEALTH = 1

    BASE_LENGTH = 3

    BASE_LINE = 10

    def __init__(self,name="Default"):
        self.serpent = [(Serpent.BASE_LINE,10),(Serpent.BASE_LINE,11),(Serpent.BASE_LINE,12)]
        Serpent.BASE_LINE += 10
        self.oldPos = (0,0)
        self.name = name
        self.loose = False
        self.dieReason = "a gagné"
        self.color = ("gray","white")
        
        self.direction = Serpent.DIRECTION[0]

        self.score = 0
        self.kill = 0
        self.health = Serpent.MAX_HEALTH
        self.healthTick = 0

    def nextCase(self):
        if (self.direction == Serpent.DIRECTION[0]):
            return (self.serpent[-1][0],self.serpent[-1][1]+1)
        elif (self.direction == Serpent.DIRECTION[1]):
            return (self.serpent[-1][0]+1,self.serpent[-1][1])
        elif (self.direction == Serpent.DIRECTION[2]):
            return (self.serpent[-1][0],self.serpent[-1][1]-1)
        if (self.direction == Serpent.DIRECTION[3]):
            return (self.serpent[-1][0]-1,self.serpent[-1][1])

    def avance(self,i,j):
        self.serpent.append((i,j))
        self.oldPos = (self.serpent[0][0],self.serpent[0][1])
        self.serpent.pop(0)
        """if (Game.PARAM_HEALTH):
            self.health -= 1"""
    def loop(self):
        (i,j) = self.nextCase()
        self.avance(i,j)
    def printScore(self):
        print("     -> Score de {0} : {1} ({3} pomme(s) + {4} kill(s)) {2}".format(self.name,self.score+self.kill,self.dieReason,self.score,self.kill))
    # Directions
    def execKey(self,direct):
        if (self.direction != Serpent.DIRECTION[Serpent.getOpposedDir(direct)]):
            self.direction = Serpent.DIRECTION[direct]
    def getOpposedDir(direct):
        if (direct == 0):
            return 2
        elif (direct == 1):
            return 3
        elif (direct == 2):
            return 0
        elif (direct == 3):
            return 1
    # Collisions
    def selfCollide(self):
        for c in range(len(self.serpent)-1):
            (x,y) = self.serpent[c]
            if (x==self.serpent[-1][0] and y==self.serpent[-1][1]):
                return True
        return False
    # Health
    def healthTick(self):
        self.healthTick +=1
        if (self.healthTick>=Serpent.TICK_PER_HEALTH):
            self.healthTick = 0
            self.decHealth()
    def decHealth(self):
        self.health -=1
    # Apple
    def eat(self):
        self.health += Serpent.APPLE_HEALTH
        self.score += 1
        if (self.health>=Serpent.MAX_HEALTH):
            self.health = Serpent.MAX_HEALTH
        (i,j) = self.nextCase()
        self.serpent.append((i,j))
    def addKill(self):
        self.kill += 1
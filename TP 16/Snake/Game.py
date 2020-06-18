from tkinter import *
from random import randint

from Snake.Serpent import *

class Game:

    LIGNES = 30
    COLONNES = 50
    CASE = 10 # Taille d'un pixel du jeu sur l'écran (en pixels :) )
    FRAME = 82 # Durée de chaque frame en ms
    #FRAME = 100

    PARAM_HEALTH = True

    APPLE_DECAY_TIME = 50

    BG_COLOR = "black"

    KEY_SET = [
        ("<Right>","<Left>","<Up>","<Down>"),
        ("d","q","z","s")
    ]
    COLOR_SET = [
        ("steel blue","light steel blue"),
        ("medium orchid","purple4"),
        ("lawn green","forest green"),
        ("bisque","bisque4")
    ]

    DIE_MESSAGE_HEALTH = "(est mort en n'ayant plus de vie)"
    DIE_MESSAGE_BORDER_COLLID = "(est mort en se prenant un mur)"
    DIE_MESSAGE_COLLIDE_HIMSELF = "(est mort en se mordant la queue)"
    DIE_MESSAGE_HIT_ANOTHER = "(est mort en touchant un joueur)"
    DIE_MESSAGE_EAT_POISON = "(est mort en s'intoxiquant)"

    def __init__(self):
        # Apples
        self.apple = (0,0)
        
        self.appleDecay = 0
        self.poisonous = []

        # Players
        self.snakes = []
        self.multiplayer = False

        self.fen = Tk()
        self.canvas = Canvas(self.fen, height=Game.LIGNES * Game.CASE, width=Game.COLONNES * Game.CASE, bg="black")
        self.canvas.pack()
    def init(self):
        self.setPixels()
        self.initSnakes()
        self.genNewApple()

        self.loop()
        self.fen.mainloop()
    def loop(self):
        for snake in self.snakes:
            # Die reason
            if (snake.selfCollide()):
                self.setDie(snake,Game.DIE_MESSAGE_COLLIDE_HIMSELF)
            if (snake.health<=0):
                self.setDie(snake,Game.DIE_MESSAGE_HEALTH)
            if (snake.serpent[-1][0]==Game.LIGNES-1 or snake.serpent[-1][0]<0 or snake.serpent[-1][1]==Game.COLONNES-1 or snake.serpent[-1][1]<0):
                self.setDie(snake,Game.DIE_MESSAGE_BORDER_COLLID)
            if (self.isOnPoison(snake)):
                self.setDie(snake,Game.DIE_MESSAGE_EAT_POISON)
            if (self.ifSnakeHitAnother(snake)):
                self.setDie(snake,Game.DIE_MESSAGE_HIT_ANOTHER)
            # Actions
            if not(snake.loose):
                if (self.snakeIsOnApple(snake)):
                    snake.eat()
                    self.genNewApple()
                else:
                    snake.loop()
        if not(self.ifGameContinue()):
            self.endOfTheGame()
            return
        else:
            self.drawSnakes()
            self.decayApple()
            self.fen.after(Game.FRAME,self.loop)
    def setDie(self,snake,reason):
        snake.loose = True
        snake.dieReason = reason
        self.hideSnake(snake)
    # Tests
    def ifGameContinue(self):
        c = 0
        for snake in self.snakes:
            if not(snake.loose):
                c+=1
        if (self.multiplayer):
            return (c>=2)
        else:
            return (c>=1)
    def isOnPoison(self,snake):
        (x,y) = snake.serpent[-1]
        for c in range(len(self.poisonous)):
            (i,j) = self.poisonous[c]
            if (x==i and y==j):
                self.poisonous.pop(c)
                return True
        return False
    def snakeIsOnApple(self,snake):
        return (snake.serpent[-1][0]==self.apple[0] and snake.serpent[-1][1]==self.apple[1])
    def ifSnakeHitAnother(self,snake):
        (x,y)=snake.serpent[-1]
        for s in self.snakes:
            if not(s==snake):
                for (i,j) in s.serpent:
                    if (x==i and y==j):
                        s.addKill()
                        return True
        return False

    # Endgame
    def endOfTheGame(self):
        if (self.multiplayer):
            for s in self.snakes:
                if not(s.loose):
                    print("{} a gagné !".format(s.name))
        else:
            print("Perdu !")
        for s in self.snakes:
            s.printScore()
    # Players
    def addPlayer(self,snake):
        if (len(self.snakes)!=0):
            self.multiplayer = True
        self.snakes.append(snake)

        # Set keybinding
        keybind = Game.KEY_SET[len(self.snakes)-1]
        self.fen.bind(keybind[0],lambda e : snake.execKey(0)) # Right
        self.fen.bind(keybind[1],lambda e : snake.execKey(2)) # Left
        self.fen.bind(keybind[2],lambda e : snake.execKey(3)) # Up
        self.fen.bind(keybind[3],lambda e : snake.execKey(1)) # Down

        color = Game.COLOR_SET[len(self.snakes)+2]
        snake.color = color
    # Apples
    def genNewApple(self):
        newPomme = self.apple
        while (newPomme[0]==self.apple[0] and newPomme[1]==self.apple[1]):
            x = randint(4,Game.LIGNES-5)
            y = randint(4,Game.COLONNES-5)
            newPomme = (x,y)
        self.apple = newPomme
        self.appleDecay = 0
        self.printPixel(newPomme[0],newPomme[1],"red")
    def decayApple(self):
        self.appleDecay +=1
        if (self.appleDecay>=Game.APPLE_DECAY_TIME):
            self.poisonous.append((self.apple[0],self.apple[1]))
            self.printPixel(self.apple[0],self.apple[1],"green")
            self.genNewApple()
            self.appleDecay = 0
        elif (self.appleDecay>=2*Game.APPLE_DECAY_TIME//3):
            self.printPixel(self.apple[0],self.apple[1],"yellow")
        elif (self.appleDecay>=Game.APPLE_DECAY_TIME//3):
            self.printPixel(self.apple[0],self.apple[1],"orange")
    # Graphics
    def setPixels(self):
        self.pixel = []
        for i in range(Game.LIGNES):
            ligne = []
            for j in range(Game.COLONNES):
                rect = self.canvas.create_rectangle(j * Game.CASE, i * Game.CASE, (j+1) * Game.CASE, (i+1) * Game.CASE, width=0, fill="black")
                ligne.append(rect)
            self.pixel.append(ligne)
    def printPixel(self,i,j,color):
        self.canvas.itemconfig(self.pixel[i][j],fill=color)
    def initSnakes(self):
        for snake in self.snakes:
            for (x,y) in snake.serpent:
                self.printPixel(x,y,snake.color[0])
            self.printPixel(snake.serpent[-1][0],snake.serpent[-1][1],snake.color[1])
    def drawSnakes(self):
        for snake in self.snakes:
            s = snake.serpent
            self.printPixel(snake.oldPos[0],snake.oldPos[1],Game.BG_COLOR)
            self.printPixel(s[-1][0],s[-1][1],snake.color[1])
            self.printPixel(s[-2][0],s[-2][1],snake.color[0])
    def hideSnake(self,snake):
        for (x,y) in snake.serpent:
            self.printPixel(x,y,Game.BG_COLOR)
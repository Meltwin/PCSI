#---------#
# Imports #
#---------#

from tkinter import *
from random import randint

#-------------------#
# Parametres du jeu #
#-------------------#

LIGNES = 30
COLONNES = 50
CASE = 10 # Taille d'un pixel du jeu sur l'écran (en pixels :) )
FRAME = 82 # Durée de chaque frame en ms

DECAY_TIME =50 # en tick
#FRAME = 1000 # Durée de chaque frame en ms

#---------------------#
# Interface graphique #
#---------------------#

# NE PAS MODIFIER #

# Création de l'interface graphique
fenetre = Tk()

canvas = Canvas(fenetre, height=LIGNES * CASE+3*CASE, width=COLONNES * CASE, bg="black")
canvas.pack()

# Création d'une matrice de pixels
pixel = []
for i in range(LIGNES):
    ligne = []
    for j in range(COLONNES):
        rect = canvas.create_rectangle(j * CASE, i * CASE, (j+1) * CASE, (i+1) * CASE, width=0, fill="black")
        ligne.append(rect)
    pixel.append(ligne)

# Change la couleur du pixel (i, j) en c
# Exemple : couleurPixel(5, 10, "white")
def couleurPixel(i, j, c):
    canvas.itemconfig(pixel[i][j], fill=c)

# FIN NE PAS MODIFIER #

#-----------------#
# Initialisations #
#-----------------#

# Variables globales
serpent = [(5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10)]
direction = "droite"
score = 0
pomme = (10,8)
pommedecay = 0
poison_apple = []
vieMax = 80
vie = 80

# Dessin initial du serpent  :
for couple in serpent:
    couleurPixel(couple[0],couple[1],"gray")
# Dessin initial de la pomme :
couleurPixel(pomme[0],pomme[1],"red")

#------------------#
# Fonctions du jeu #
#------------------#

# Cette fonction retourne True si l case (i, j) n'est pas disponible
# (ou n'existe pas). Retourne False sinon.
def collision(i, j):
    for couple in serpent:
        
    return (i>=LIGNES or i<0 or j>= COLONNES or j<0)

# Cette fonction retourne un couple (i, j) correspondant à la prochaine
# case qui sera atteinte par le serpent, en fonction de la position de
# sa tête et de la direction
def prochaineCase():
    t = serpent[-1]
    if (direction == "haut"):
        return (t[0]-1, t[1])
    elif (direction == "bas"):
        return (t[0]+1, t[1])
    elif (direction == "gauche"):
        return (t[0], t[1]-1)
    else:
        return (t[0], t[1]+1)

# Fait avancer le serpent vers la case i j
# On modifiera serpent et certains pixels
def avance(i, j):
    global serpent
    couleurPixel(i,j,"gray")
    couleurPixel(serpent[0][0],serpent[0][1],"black")
    serpent.append((i,j))
    serpent.pop(0)
    print("Vie : {0}/{1}".format(vie,vieMax))
    return

# Similaire à avance mais une pomme se trouve en i j :
# le serpent grandit
def mange(i, j):
    global serpent
    global score
    global vie
    couleurPixel(i,j,"gray")
    serpent.append((i,j))
    vie = vieMax
    score += 1
    return
# Cherche une case disponible et y place une pomme
def nouvellePomme():
    global pomme
    newPomme = pomme
    while (newPomme[0]==pomme[0] and newPomme[1]==pomme[1]):
        x = randint(0,LIGNES-1)
        y = randint(0,COLONNES-1)
        newPomme = (x,y)
    couleurPixel(newPomme[0],newPomme[1],"red")
    pomme = newPomme
    return
def decVie():
    global vie
    vie -= 1
    return

def decayApple():
    global pommedecay
    pommedecay+=1
    if (pommedecay>=DECAY_TIME):
        poison_apple.append((pomme[0],pomme[1]))
        couleurPixel(pomme[0],pomme[1],"green")
        nouvellePomme()
        pommedecay = 0
    elif (pommedecay>=2*DECAY_TIME//3):
        couleurPixel(pomme[0],pomme[1],"yellow")
    elif (pommedecay>=DECAY_TIME//3):
        couleurPixel(pomme[0],pomme[1],"orange")
def isOnPoisonous(i,j):
    global poison_apple
    for couple in poison_apple:
        if (couple[0]==i and couple[1]==j):
            return True
    return False
#-------------------#
# Boucle principale #
#-------------------#

# boucle() contient le code qui est exécuté à chaque frame
def boucle():
    (i, j) = prochaineCase()
    if collision(i, j) or vie<=0 or isOnPoisonous(i,j):
        print("PERDU !!!")
        print("Score : {}".format(score))
        return # Le jeu s'arrete
    else:
        decVie()
        decayApple()
        if (pomme[0]==i and pomme[1]==j):
            mange(i,j)
            nouvellePomme()
        else:
            avance(i,j)
    fenetre.after(FRAME, boucle) # La boucle est relancée après un certain temps

#---------------------#
# Evenements claviers #
#---------------------#


# Ces fonctions sont exécutées lorsque le joueur
# appuie sur une touche
# global direction est ajouté pour qu'elles puissent
# modifier la variable globale direction

def toucheGauche(event):
    global direction
    if (direction!="droite"):
        direction = "gauche"
    return

def toucheDroite(event):
    global direction
    if (direction!="gauche"):
        direction = "droite"
    return

def toucheBas(event):
    global direction
    if (direction!="haut"):
        direction = "bas"
    return

def toucheHaut(event):
    global direction
    if (direction!="bas"):
        direction = "haut"
    return

# Connexion des évenements claviers Tk avec nos fonctions
fenetre.bind("<Left>", toucheGauche)
fenetre.bind("<Right>", toucheDroite)
fenetre.bind("<Up>", toucheHaut)
fenetre.bind("<Down>", toucheBas)

#------------------------#
# Lancement du programme #
#------------------------#

boucle()
fenetre.mainloop()

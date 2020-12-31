#---------#
# Imports #
#---------#

from tkinter import Tk, Canvas
from random import randint

#-------------------#
# Parametres du jeu #
#-------------------#

LIGNES = 30
COLONNES = 50
CASE = 10 # Taille d'un pixel du jeu sur l'écran (en pixels :) )
FRAME = 150 # Durée de chaque frame en ms

#---------------------#
# Interface graphique #
#---------------------#

# NE PAS MODIFIER #

# Création de l'interface graphique
fenetre = Tk()

canvas = Canvas(fenetre, height=LIGNES * CASE, width=COLONNES * CASE, bg="black")
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
# direction = "droite"
# score = ...
# pomme = ...

# Dessin initial du serpent  :

# Dessin initial de la pomme :

#------------------#
# Fonctions du jeu #
#------------------#

# Cette fonction retourne True si l case (i, j) n'est pas disponible
# (ou n'existe pas). Retourne False sinon.
def collision(i, j):
    return False

# Cette fonction retourne un couple (i, j) correspondant à la prochaine
# case qui sera atteinte par le serpent, en fonction de la position de
# sa tête et de la direction
def prochaineCase():
    return (0, 0)

# Fait avancer le serpent vers la case i j
# On modifiera serpent et certains pixels
def avance(i, j):
    global serpent
    return

# Similaire à avance mais une pomme se trouve en i j :
# le serpent grandit
def mange(i, j):
    global serpent
    return

# Cherche une case disponible et y place une pomme
def nouvellePomme():
    global pomme
    return

#-------------------#
# Boucle principale #
#-------------------#

# boucle() contient le code qui est exécuté à chaque frame
def boucle():
    (i, j) = prochaineCase()
    if collision(i, j):
        print("PERDU !!!")
        return # Le jeu s'arrete
    
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
    return

def toucheDroite(event):
    global direction
    return

def toucheBas(event):
    global direction
    return

def toucheHaut(event):
    global direction
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

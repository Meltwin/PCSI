from turtle import *
import math
# rectangle : dessine un rectangle x*y
# arg : int x, int y
def rectangle(x,y):
    down()
    fd(x)
    right(90)
    fd(y)
    right(90)
    fd(x)
    right(90)
    fd(y)
    up()
    
def polygone(n,x):
    down()
    for i in range(n):
        fd(x)
        right(360/n)
    up()
def polygone2(n,x):
    down()
    b = False
    for i in range(n):
        if not(b):
            color("blue")
            b= True
        else:
            color("red")
            b=False
        fd(x)
        right(360/n)
    up()
def cercle(r):
    x = r*2*math.pi/200
    polygone2(200,x)
color("red")
cercle(100)

exitonclick()

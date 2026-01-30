import turtle
from turtle import *
t = Turtle()

t.speed(1000)


""" for i in range(60):
   t.forward(100)
   t.left(90)
   t.right(5) """

length = 100
rotate = 90
def square(x,y):
    for i in range (4):
      t.forward(x)
      t.left(y)
square(100,90)
 

turtle.done()
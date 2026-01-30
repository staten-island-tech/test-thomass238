import turtle
from turtle import *
t = Turtle()

t.forward(200)
turtle.done()

def square(x):
    t.forward(x)
    t.left(90) 
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90) 
    t.forward(x)
    t.left(90)
square(200)
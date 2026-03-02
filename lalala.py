import turtle
from turtle import *
t = Turtle()

t.speed(1000)


# for i in range(60):
#    t.forward(100)
#    t.left(90)
#    t.right(5) 

# sidelength = 100
# # rotate = 90

def square(x,y):
    for i in range (4):
      t.forward(x)
      t.left(y)

# def doublesquare(iRange):
#     length = 5
#     for i in range(iRange):
#         square(length, 90)
#         length += 25
# doublesquare(5)

def squarespiral(iRange):
    length = 100
    angle = 90
    for i in range(iRange):
        square(length, angle)
        length += 5
        angle += 5        
        

squarespiral(60)

   

turtle.done()
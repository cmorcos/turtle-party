# turtle party project

import turtle

turtle.color("blue")

turtle.width(2)
turtle.speed(0)

def square(size):
  for i in range(4):
    turtle.forward(size)
    turtle.right(90)

def rectangle(width, height):
  for i in range(2):
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)

def triangle(size):
  for i in range(3):
    turtle.forward(size)
    turtle.left(120)
  
def house(lineLength):
  square(lineLength)
  triangle(lineLength)

def octagon(sideLength):
  for i in range(8):
    turtle.forward(sideLength)
    turtle.left(45)
  
def stop(sideLength):
  octagon(sideLength)
  turtle.forward(3 * sideLength / 8)
  rectangle(sideLength * (1/5), sideLength * 2)
  
stop(50)

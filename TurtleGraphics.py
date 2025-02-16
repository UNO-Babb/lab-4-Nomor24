#TurtleGraphics.py
#Name: Noah 
#Date:
#Assignment:

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(bob,sides):
    for s in range(sides):
        bob.forward(50)
        bob.right(360/sides)

def fillCorner(george, corner):
    drawSquare(george, 100)
    
    if corner == 1:
        george.begin_fill()
        drawSquare(george, 50)
        george.end_fill()
    
    elif corner == 2:
        george.forward(50)
        george.begin_fill()
        drawSquare(george, 50)
        george.end_fill()
    elif corner == 3:
        george.right(90)
        george.forward(50)
        george.left(90)
        george.begin_fill()
        drawSquare(george, 50)
        george.end_fill()
    elif corner == 4:
        george.right(90)
        george.penup()
        george.forward(50)
        george.left(90)
        george.forward(50)
        george.pendown()
        george.begin_fill()
        drawSquare(george, 50)
        george.end_fill()
    
def squaresInSquares(amy, num):
    size = 100
    
    
    for n in range (num):
        drawSquare(amy, size)
        size = size-10
        amy.penup()
        amy.forward(5)
        amy.right(90)
        amy.forward(5)
        amy.left(90)
        amy.pendown()
    
        
    
    

def main():
    myTurtle = turtle.Turtle()
    
    #drawSquare(myTurtle, 100)
    
    # drawPolygon(myTurtle, 5) #draws a pentagon
    # drawPolygon(myTurtle, 8) #draws an octogon

    # fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    #fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    #squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    #squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()

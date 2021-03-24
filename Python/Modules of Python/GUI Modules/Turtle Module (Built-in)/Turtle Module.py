"""
Turtle Module is for Automated GUIs.
"""

import turtle
import random
from turtle import Screen, Turtle

# Topic: Basic Usage
game = turtle.Turtle()  # brought the class
game.color("red")  # given color
game.pensize(5)  # sets the thickness
game.shape("turtle")  # shape for the object

# SubTopic: Turtle Movements
game.forward(100)  # 100 means pixels no,
game.left(90)
game.penup()  # lifts the pen
game.forward(100)
game.left(90)
game.pendown()  # puts the pen back down
game.forward(100)
game.left(90)
game.forward(100)

# Topic: Filling the Shapes
game1 = turtle.Turtle()
game1.color("red", "blue")  # blue is the fill color

game1.width(5)  # same like pensize

game1.begin_fill()  # to fill the shape
game1.circle(50)  # sets the shape size
game1.end_fill()  # complete the fill

for x in range(4):  # this will draw a square filled in
    game1.forward(100)
    game1.right(90)

game1.end_fill()

game1.setpos(100, -50)  # this sets the position by coordinates

# Topic: Filling many Shapes
colors = ["red", "blue", "green", "purple", "yellow", "orange", "black"]

game2 = turtle.Turtle()
game2.color("red", "blue")

for x in range(5):
    randColor = random.randrange(0, len(colors))  # selects the color from line
    rand1 = random.randrange(-300, 300)  # sets the random coordinates
    rand2 = random.randrange(-300, 300)

    game2.color(colors[randColor], colors[random.randrange(0, len(colors))])  # selects the color

    game2.penup()
    game2.setpos((rand1, rand2))
    game2.pendown()

    game2.begin_fill()
    game2.circle(random.randrange(0, 80))  # selects the size for circle
    game2.end_fill()

# Setting the heading of the turtle simply faces it a certain direction

# Topic: Key Movements
game3 = Turtle()
game3.speed(0)
game3.width(5)
colors = ["red", "blue", "green", "yellow", "black"]  # select any color


def up():
    game3.setheading(90)  # turns up
    game3.forward(100)


def down():
    game3.setheading(270)  # turns down
    game3.forward(100)


def left():
    game3.setheading(180)  # turns left
    game3.forward(100)


def right():
    game3.setheading(0)  # turns right
    game3.forward(100)


def clickLeft(x, y):  # make sure to have parameters x, y
    game3.color(random.choice(colors))


def clickRight(x, y):
    game3.stamp()


turtle.listen()  # this accepts the events

turtle.onscreenclick(clickLeft, 1)  # 1:Left Mouse Button, 2: Middle Mouse Button
turtle.onscreenclick(clickRight, 3)  # 3: Right Mouse Button

turtle.onkey(up, "Up")  # This will call the up function if the "Left" arrow key is pressed
turtle.onkey(down, "Down")
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")

turtle.mainloop()  # this will make sure the program continues to run

# Topic: Drawing with Mouse
screen = Screen()
game4 = Turtle()
game4.shape("square")
game4.speed(-1)


def dragging(x, y):  # these parameters will be the mouse position
    game4.ondrag(None)
    game4.setheading(game4.towards(x, y))
    game4.goto(x, y)
    game4.ondrag(dragging)


def clickRight(x, y):
    game4.clear()


def main():  # this will run the program
    turtle.listen()

    game4.ondrag(dragging)  # when we drag the turtle object call dragging
    turtle.onscreenclick(clickRight, 3)  # 1.left 2.middle 3.right

    screen.mainloop()  # this will continue running main()


main()

# Documentation: https://docs.python.org/3/library/turtle.html

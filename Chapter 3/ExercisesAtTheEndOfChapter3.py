import turtle
import time

window = 0

def exercise381():
    for i in range(1000):
        print("We like Python's turtles!")

def exercise382():
    pass
    # I'm not sure what this cellphone is that they're talking about.
    # I think it's a typo, or I don't understand their intent.
    # Moving on...

def exercise383():
    months = ["January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"]
    for month in months:
        print("One of the months of the year is " + month)

def exercise384():
    tess = turtle.Turtle()
    tess.left(3645)
    # https://docs.python.org/2/library/turtle.html#turtle.heading
    print("Tess's final heading is " + str(tess.heading()))
    time.sleep(2)
    tess.hideturtle()
    del tess


def exercise385():
    xs = [12, 10, 32, 3, 55, 17, 42, 99, 20]

    for x in xs:
        print(str(x))

    for x in xs:
        # Python's exponentiation operator is ** not ^ as in a lot of
        # programming languages.
        print("x=" + str(x) + " x^2=" + str(x**2))

    total = 0
    for x in xs:
        total = total + x
    print("Total = " + str(total))

    product = 1     # don't start with 0, because multiplying by 0 equals 0
    for x in xs:
        product = product * x
    print("The product = " + str(product))

def exercise386():
    tess = turtle.Turtle()
    # triangle
    for i in range(3):
        tess.forward(100)
        tess.left(120)
    # square
    for i in range(4):
        tess.forward(100)
        tess.left(90)
    # hexagon
    # http://www.math.com/school/subject3/lessons/S3U2L1DP.html
    for i in range(6):
        tess.forward(100)
        tess.left(60)
    # octagon
    for i in range(8):
        tess.forward(100)
        tess.left(45)
    time.sleep(2)
    tess.clear()
    tess.hideturtle()
    del tess


def exercise387():
    turns = [160, -43, 270, -97, -43, 200, -940, 17, -86]
    pirate = turtle.Turtle()
    for turn in turns:
        pirate.left(turn)
        pirate.forward(100)
    time.sleep(2)
    pirate.clear()
    pirate.hideturtle()
    del pirate


def exercise388():
    turns = [160, -43, 270, -97, -43, 200, -940, 17, -86]
    pirate = turtle.Turtle()
    for turn in turns:
        pirate.left(turn)
        pirate.forward(100)
        print("Pirate's heading is " + str(pirate.heading()))
    time.sleep(2)
    pirate.clear()
    pirate.hideturtle()
    del pirate

def exercise3811():
    # A litte about the geometry of pentagons (5-pointed stars)
    # http://proofsfromthebook.com/2013/08/04/angle-sum-of-a-pentagram/
    tess = turtle.Turtle()
    # Since the exercise didn't specify which corner to start at,
    # start at the top-left corner and draw the straight, left-to-right
    # line first since turtle are pointed that way by default.
    for i in range(5):
        tess.forward(100)
        tess.right(144)
    time.sleep(2)
    tess.clear()
    tess.hideturtle()
    del tess



if __name__ == '__main__':
    # Create one turtle Screen for all exercises to use.
    window = turtle.Screen()

#    exercise381()
#    exercise382()
#    exercise383()
#    exercise384()
#    exercise385()
#    exercise386()
#    exercise387()
#    exercise388()
    exercise3811()

    window.bye()


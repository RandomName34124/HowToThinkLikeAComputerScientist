import turtle


def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    wn.title("Tess & Alex")

    # Create a tess turtle and set a few custom options (color & pensize)
    tess = turtle.Turtle()
    tess.color("hotpink")
    tess.pensize(5)

    # Create an alex turtle and use the default options
    alex = turtle.Turtle()

    # Move tess along a triangular path
    tess.forward(80)
    tess.left(120)
    tess.forward(80)
    tess.left(120)
    tess.forward(80)
    tess.left(120)

    # Move tess away from the end of the triangle
    tess.right(180)     # turn tess 180 degrees
    tess.forward(80)

    # Move alex along a square path
    alex.forward(50)
    alex.left(90)
    alex.forward(50)
    alex.left(90)
    alex.forward(50)
    alex.left(90)
    alex.forward(50)
    alex.left(90)

    # Start the screen's main loop.  This loop will run until the close
    # button is pressed.
    wn.mainloop()


if __name__ == '__main__':
    main()

import turtle
# turtle module documentation
# https://docs.python.org/3.5/library/turtle.html


def main():
    # Create the screen/window on which we'll draw & move turtles
    window = turtle.Screen()
    window.bgcolor("lightgreen")

    # Create and customize a tess turtle
    tess = turtle.Turtle()
    tess.shape("turtle")
    tess.color("blue")

    tess.penup()
    moveSize = 20
    for i in range(30):
        tess.stamp()
        moveSize = moveSize + 3
        tess.forward(moveSize)
        tess.right(24)


if __name__ == '__main__':
    main()

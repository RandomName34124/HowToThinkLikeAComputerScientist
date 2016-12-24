# Friday, December 23, 2016
# http://openbookproject.net/thinkcs/python/english3e/hello_little_turtles.html

import turtle


def main():
    # Program extension challenge #1: modify the program so that before it
    # creates the window, it prompts the user to enter the desired background
    # color.
    try:
        bgColor = input("Please enter a background color")
    except KeyboardInterrupt:
        # A KeyboardInterrupt will occur if the user clicks the cancel
        # button displayed as a result of the previous input command.
        # For this program, we're going to assign a default background color
        # More on errors & exceptions later
        bgColor = "white"

    # Program extension challenge #2: get a color for tess
    try:
        tessColor = input("Please enter a color for Tess")
    except KeyboardInterrupt:
        tessColor = "blue"

    # Program extension challenge #3: get a pen size for drawing tess
    try:
        tessPenSize = input("Please input a pen size (a number)")
        tessPenSize = int(tessPenSize)
    except (KeyboardInterrupt, ValueError):
        tessPenSize = 3

    # Create the screen on which turtles will be drawn
    wn = turtle.Screen()
    wn.title("Hello, Tess!")

    # This is another point in which an exception may be generated, and once
    # again, it's related to the user's input.  If the user enters a
    # misspelled color or a color that the program doesn't recognize, then
    # a turtle.TurtleGraphicsError will be raised.  We need to catch it
    # or it will cause the program to abort.
    try:
        wn.bgcolor(bgColor)
    except turtle.TurtleGraphicsError:
        # Set the background color to red if we caught the exception
        wn.bgcolor("red")

    tess = turtle.Turtle()
    try:
        tess.color(tessColor)
    except turtle.TurtleGraphicsError:
        tess.color("blue")
    tess.pensize(tessPenSize)

    tess.forward(50)    # move 50 units forward
    tess.left(120)      # turn 120 degrees to the left
    tess.forward(50)    # move another 50 units

    wn.mainloop()


if __name__ == '__main__':
    main()
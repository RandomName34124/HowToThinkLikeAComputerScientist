import turtle

def main():
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    wn.title("Hello, Tess!")

    tess = turtle.Turtle()
    tess.color("blue")
    tess.pensize(3)

    tess.forward(50)
    tess.left(120)
    tess.forward(50)

    wn.mainloop()

if __name__ == '__main__':
    main()
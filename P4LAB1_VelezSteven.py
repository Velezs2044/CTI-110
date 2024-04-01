import turtle

win = turtle.Screen()
t = turtle.Turtle()

t.pensize(100)

t.pencolor("green")

for item in range(3):
    #Action to happen.
    turtle.forward(300)
    turtle.left(120)

for item in range(4):
    turtle.forward(300)
    turtle.left(90)

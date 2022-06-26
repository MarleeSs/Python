import turtle

a = turtle.Turtle
wn = turtle.Screen()
wn.title('Python')


a.speed(100)

for i in range(100):
    a.forward(100)
    a.right(30)
    a.forward(20)
    a.left(60)
    a.forward(50)
    a.forward(30)

    a.penup()
    a.setposition(0, 0)
    a.pendown()

    a.right(2)

a.end_fill()
wn.exitonclick()
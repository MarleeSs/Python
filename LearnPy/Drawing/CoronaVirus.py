import turtle
wdw = turtle.Screen()
wdw.title("Python")

x = 0
y = 0

turtle.bgcolor("#191A19")
turtle.speed(0)
turtle.pencolor("#49FF00")
turtle.penup()
turtle.goto(0, 200)
turtle.pendown()

while True:
    turtle.forward(x)
    turtle.right(y)
    x += 3
    y += 1
    if y == 200:
        break
turtle.exitonclick()

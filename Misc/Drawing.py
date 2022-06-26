import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen() .bgcolor("black")
t.color("white")
t.speed(0)
t.width(5)
n = 2000
h = 0
for i in range (200) :
    t.forward(i*2)
    t.right(59)
    c = colorsys.hsv_to_rgb(h,1,0.8)
    h += 1/n
    t.color(c)

turtle.exitonclick()
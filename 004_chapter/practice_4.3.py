
import turtle, math


def triangle(t, length, angle):
    new_length = length * math.sin(angle * math.pi / 180)
    t.rt(angle)
    t.fd(length)
    t.lt(90 + angle)
    t.fd(2 * new_length)
    t.lt(90 + angle)
    t.fd(length)
    t.lt(180 - angle)

def pie(t, n, length):
    angle = 360 / n
    for i in range(n):
        triangle(t, length, angle/2)
        t.lt(angle)

def draw_pie(t, n, length):
    pie(t, n, length)

def move(t, length):
    t.pu()
    t.fd(length)
    t.pd()


bob = turtle.Turtle()

move(bob, -150)
draw_pie(bob, 5, 60)

move(bob, 150)
draw_pie(bob, 6, 60)

move(bob, 150)
draw_pie(bob, 7, 60)

bob.hideturtle()
turtle.mainloop()

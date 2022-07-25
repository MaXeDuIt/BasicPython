
import turtle, math

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle):
    arc_length = (math.pi * r / 180) * abs(angle)
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n
    t.lt(step_angle / 2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle / 2)

def petal(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        t.lt(180 - angle)

def flower(t, n, r, angle):
    for i in range(n):
        petal(t, r, angle)
        t.lt(float(360 / n))

def move(t, length):
    t.pu()
    t.fd(length)
    t.pd()


bob = turtle.Turtle()
move(bob, -250)
flower(bob, 7, 100, 60)

move(bob, 250)
flower(bob, 10, 80, 80)

move(bob, 250)
flower(bob, 20, 160, 20)

bob.hideturtle()
turtle.mainloop()

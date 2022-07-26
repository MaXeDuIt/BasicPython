
import turtle, math

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t, n, length):
    angle = 360 / n
    polyline(t, n, length, angle)

def circle(t, r):
    arc(t, r, 360)

def arc(t, r, angle):
    arc_length = (math.pi * r / 180) * abs(angle)
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n
    t.lt(step_angle / 2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle / 2)

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

bob = turtle.Turtle()
# square(bob, 175)
# polygon(bob, 7, 120)
# circle(bob, 150)
# arc(bob, 100, 360)
radius = 100
bob.pu()
bob.fd(radius)
bob.lt(90)
bob.pd()
circle(bob, radius)

turtle.mainloop()

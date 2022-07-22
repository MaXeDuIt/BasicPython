
import turtle, math

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def circle(t, r):
    n = 50
    circumference = 2 * math.pi * r
    length = circumference / n
    polygon(t, n, length)

bob = turtle.Turtle()
# square(bob, 175)
# polygon(bob, 7, 120)
circle(bob, 50)

turtle.mainloop()

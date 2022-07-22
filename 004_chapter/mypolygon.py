
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
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 1
    length = circumference / n
    polygon(t, n, length)


bob = turtle.Turtle()
# square(bob, 175)
# polygon(bob, 7, 120)
circle(bob, 150)

turtle.mainloop()

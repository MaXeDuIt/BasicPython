
import turtle

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t, n, length):
    for i in range(n):
        t.fd(length)
        t.lt(360 / n)

bob = turtle.Turtle()
# square(bob, 175)
polygon(bob, 7, 120)

turtle.mainloop()

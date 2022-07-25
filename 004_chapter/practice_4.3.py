
import turtle


def triangle(t, length, angle):
    t.rt(angle)
    t.fd(length)
    t.lt(90 + angle)
    t.fd(2 * length)
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

bob = turtle.Turtle()
draw_pie(bob, 5, 40)

bob.hideturtle()
turtle.mainloop()
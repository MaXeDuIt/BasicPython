
import turtle

def draw_spiral(t, n, length=3, a=0.1, b=0.0002):
    theta = 0
    for i in range(n):
        t.fd(length)
        dtheta = 1 / (a + b * theta)
        t.lt(dtheta)
        theta += dtheta

bob = turtle.Turtle()
draw_spiral(bob, n=1000)

bob.hideturtle()
turtle.mainloop()
import turtle
from math import atan2, sqrt, pi


def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle):
    arc_length = (pi * r / 180) * abs(angle)
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n
    t.lt(step_angle / 2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle / 2)

def circle(t, r):
    arc(t, r, 360)

def move(t, length):
    t.pu()
    t.fd(length)
    t.pd()


def forward(t, length):
    t.fd(length)

def back(t, length):
    t.bk(length)

def left(t, angle=90):
    t.lt(angle)

def right(t, angle=90):
    t.rt(angle)

def pendown(t):
    t.pd()

def penup(t):
    t.pu()


def forward_left(t, length, angle=90):
    forward(t, length)
    left(t, angle)

def forward_back(t, length):
    forward(t, length)
    back(t, length)

def skip(t, length):
    penup(t)
    forward(t, length)
    pendown(t)

def stump(t, length, angle=90):
    left(t, angle)
    forward(t, length)
    right(t, angle)

def hollow(t, length):
    left(t)
    skip(t, length)
    right(t)


def post(t, length):
    left(t)
    forward_back(t, length)
    right(t)

def beam(t, length, height):
    hollow(t, length*height)
    forward_back(t, length)
    hollow(t, -length*height)

def hangman(t, length, height):
    stump(t, length*height)
    forward_back(t, length)
    left(t)
    back(t, length*height)
    right(t)

def diagonal(t, x, y):
    angle = atan2(y, x) * 180 / pi
    dist = sqrt(x**2 + y**2)
    left(t, angle)
    forward_back(t, dist)
    right(t, angle)

def vshape(t, length, height):
    diagonal(t, -length/2, length*height)
    diagonal(t, length/2, length*height)

def bump(t, length, height):
    stump(t, length*height)
    arc(t, length/2, 180)
    left(t)
    forward_left(t, length*height+length)

def draw_d(t, length):
    bump(t, 2*length, 0)
    skip(t, length)

def draw_h(t, length):
    post(t, 2*length)
    hangman(t, length, 1)
    skip(t, length)
    post(t, 2*length)

def draw_e(t, length):
    hangman(t, length, 2)
    hangman(t, length, 1)
    forward(t, length)

def draw_l(t, length):
    post(t, 2*length)
    forward(t, length)

def draw_o(t, length):
    skip(t, length)
    circle(t, length)
    skip(t, length)

def draw_r(t, length):
    bump(t, length, 1)
    skip(t, length/2)
    diagonal(t, -length/2, length)

def draw_w(t, length):
    skip(t, length/2)
    vshape(t, length, 2)
    skip(t, length)
    vshape(t, length, 2)
    skip(t, length/2)


bob = turtle.Turtle()
size = 30
move(bob, -350)
for i in [draw_h, draw_e, draw_l, draw_l, draw_o, skip, draw_w, draw_o, draw_r, draw_l, draw_d]:
    i(bob, size)
    skip(bob, size)

bob.hideturtle()
turtle.mainloop()

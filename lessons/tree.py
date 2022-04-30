import turtle as t
from random import random


def tree(x: float, y: float) -> None:
    t.penup()
    t.goto(x, y)
    t.pendown()
    TRUNK = 100.0
    UP = 90.0
    branch(TRUNK, UP)
    t.update()


def branch(length: float, angle: float) -> None:
    t.setheading(angle)
    t.forward(length)
    if length < 3.0:
        ...
    else:
        nature: float = random() * 0.5
        branch(length * 0.55 + nature, angle + 25.0 * nature)
        branch(length * 0.60, angle - 20.0)
    t.setheading(angle + 180)
    t.forward(length)


t.tracer(0, 0)  # This only updates when you call t.update()
t.speed(0)
t.getscreen().onclick(tree)
t.done()
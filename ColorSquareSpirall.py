#SquareSpirall - Desenha uma espiral quadrangular

import turtle
t = turtle.Pen()
colors = ["red", "yellow", "blue", "green"]
for x in range(1000):
    t.pencolor(colors[x%4])
    t.forward(x)
    t.left(91)

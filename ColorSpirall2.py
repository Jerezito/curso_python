#SquareSpirall - Desenha uma espiral quadrangular

import turtle
t = turtle.Pen()
turtle.bgcolor("red")
colors = ["black", "yellow", "blue", "green"]
for x in range(1000):
    t.pencolor(colors[x%4])
    t.circle(x)
    t.left(91)

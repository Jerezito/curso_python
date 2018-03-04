#SquareSpirall - Desenha uma espiral quadrangular

import turtle
t = turtle.Pen()
t.pencolor("red")
for x in range(1000):
    t.forward(x)
    t.left(91)

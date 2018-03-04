#SquareSpirall - Desenha uma espiral quadrangular

import turtle
t = turtle.Pen()
turtle.bgcolor("black")
# Voce pode escolher entre 2 e 6 lados para obter algumas formas interessantes!
sides = 6
colors = ["red", "yellow", "blue", "orange", "green", "purple"]
for x in range(1000):
    t.pencolor(colors[x%sides])
    t.forward(x * 3 /sides + x)
    t.left(360/sides + 1)
    t.width(x*sides/200)

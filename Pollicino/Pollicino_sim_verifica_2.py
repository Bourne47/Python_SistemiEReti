import turtle

turtle.speed(100)
def disegna_quadrato(lato):
    for _ in range(4):
        turtle.pendown()
        turtle.forward(lato)
        turtle.left(90)
        turtle.penup()
for _ in range(4):
    for _ in range(4):
        disegna_quadrato(10)
        turtle.forward(10)
    turtle.backward(40)
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)
turtle.hideturtle()
turtle.mainloop()
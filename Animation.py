import turtle

turtle.bgcolor("black")
turtle.speed(0)
turtle.hideturtle()

Colors = ["yellow","green","blue","red"]

for i in range(500):
    for x in Colors:
        turtle.color(x)
        turtle.forward(i)
        turtle.left(91)
        turtle.tracer(10)

turtle.mainloop()
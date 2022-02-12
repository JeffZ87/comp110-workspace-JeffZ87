from turtle import Turtle, colormode, done

colormode(255)
bob: Turtle = Turtle()
leo: Turtle = Turtle()
# leo.hideturtle()
leo.color(255, 204, 250)
bob.color(0, 0, 0)
leo.speed(5)
bob.speed(20)

leo.penup()
bob.penup()
leo.goto(-150, -120)
bob.goto(-150, -120)
bob.pendown()
leo.pendown()

leo.begin_fill()
# code for shape to be filled 
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1

side_length: float = 300


leo.end_fill()
j: int = 0
while (j < 9):
    bob.forward(side_length)
    bob.left(121)
    j = j + 1
    side_length = side_length * 0.97
done()
import turtle

s = turtle.Screen()
t = turtle.Turtle()

s.bgcolor('light green')

t.pencolor('dark green')
t.pensize(10)

t.penup()
t.goto(0,200)
t.pendown()
t.left(90)
t.circle(30,360)

t.penup()
t.goto(-30,170)
t.pendown()
t.left(90)
t.circle(30,360)
t.penup()

t.left(90)
t.goto(-60,50)
t.pendown()
t.circle(30,360)

t.penup()
t.left(90)
t.goto(-30,-40)
t.pendown()
t.circle(30,360)
t.penup()

t.goto(-65,-70)
t.pendown()
t.forward(70)
t.penup()

t.goto(-65,-70)
t.right(90)
t.pendown()
t.forward(50)

t.penup()
t.left(90)
t.pendown()
t.forward(30)

t.right(180)
t.circle(35,-180)
t.left(180)
t.forward(35)
t.penup()

t.goto(-150,25)
t.pendown()
t.forward(60)
t.right(120)
t.forward(60)
t.right(120)
t.forward(120)
t.penup()

t.goto(-210,25)
t.right(60)
t.pendown()
t.forward(60)
t.penup()

t.goto(50,70)
t.left(120)
t.right(60)
t.pendown()
t.forward(120)
t.left(120)
t.forward(60)
t.right(120)
t.forward(60)
t.left(120)
t.forward(120)

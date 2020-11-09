import turtle

pencere = turtle.Screen()
pencere.title("Pin Pong Oyunu")
pencere.bgcolor("turquoise")
pencere.setup(width=800, height=600)
pencere.tracer(0)

raket1 = turtle.Turtle()
raket1.speed(0)
raket1.shape("square")
raket1.color("black")
raket1.penup()
raket1.goto(-350, 0)
raket1.shapesize(5, 1)

raket2 = turtle.Turtle()
raket2.speed(0)
raket2.shape("square")
raket2.color("black")
raket2.penup()
raket2.goto(350, 0)
raket2.shapesize(5, 1)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.dx = 0.15
ball.dy = 0.15

yazi = turtle.Turtle()
yazi.speed(0)
yazi.color("red")
yazi.penup()
yazi.goto(0, 260)
yazi.write("Oyuncu A: 0      Oyuncu B: 0", align="center", font=("Courier", 24, "bold"))
yazi.hideturtle()
puanA = 0
puanB = 0

def raket1_up():
    y = raket1.ycor()
    y = y + 20
    raket1.sety(y)

def raket1_down():
    y = raket1.ycor()
    y = y - 20
    raket1.sety(y)

def raket2_up():
    y = raket2.ycor()
    y = y + 20
    raket2.sety(y)

def raket2_down():
    y = raket2.ycor()
    y = y - 20
    raket2.sety(y)


pencere.listen()
pencere.onkeypress(raket1_up,"w")
pencere.onkeypress(raket1_down,"s")
pencere.onkeypress(raket2_up,"Up")
pencere.onkeypress(raket2_down,"Down")


while True:
    pencere.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy = ball.dy * -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx = ball.dx * -1
        puanA = puanA + 1
        yazi.clear()
        yazi.write("Oyuncu A: {}      Oyuncu B: {}".format(puanA, puanB), align="center", font=("Courier", 24, "bold"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx = ball.dx * -1
        puanB = puanB + 1
        yazi.clear()
        yazi.write("Oyuncu A: {}      Oyuncu B: {}".format(puanA, puanB), align="center", font=("Courier", 24, "bold"))

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < raket2.ycor() + 60 and ball.ycor() > raket2.ycor() - 60):
        ball.setx(340)
        ball.dx = ball.dx * -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < raket1.ycor() + 60 and ball.ycor() > raket1.ycor() - 60):
        ball.setx(-340)
        ball.dx = ball.dx * -1

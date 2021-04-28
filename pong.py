# Pong
# By @dlm317
# Part 1: getting started

import turtle
import winsound

win = turtle.Screen()
win.title("Pong by @dlm317")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0) # it stops the window to update

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #sets speed to max available
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) #sets speed to max available
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0) #sets speed to max available
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1 #every time the ball moves, it will move 2px
ball.dy = 1

# Functions to move paddle_a
def paddle_a_up():
    y = paddle_a.ycor()
    y += 40
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 40
    paddle_a.sety(y)

# Functions to move paddle_b
def paddle_b_up():
    y = paddle_b.ycor()
    y += 40
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 40
    paddle_b.sety(y)

# Keyboard binding
win.listen()

# paddle a binding
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")

#paddle b binding
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Border checking
    # Check coords, if near edge bounce
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 #this reverses direction
        winsound.PlaySound("C:/Users/Laura/Documents/Proyectos/Pong/legal.wav", winsound.SND_ASYNC)
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 #this reverses direction
        winsound.PlaySound("C:/Users/Laura/Documents/Proyectos/Pong/legal.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle a and ball collisions
    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40:
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("C:/Users/Laura/Documents/Proyectos/Pong/legal.wav", winsound.SND_ASYNC)

    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40:
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("C:/Users/Laura/Documents/Proyectos/Pong/legal.wav", winsound.SND_ASYNC)

    # Paddle_a  y boundaries
    if paddle_a.ycor() > 260:
        paddle_a.sety(270)

    if paddle_a.ycor() < -260:
        paddle_a.sety(-260)

    # Paddle_b y boundaries
    if paddle_b.ycor() > 260:
        paddle_b.sety(260)

    if paddle_b.ycor() < -260:
        paddle_b.sety(-260)

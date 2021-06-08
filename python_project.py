import turtle
win=turtle.Screen()
win.title("Pong Game by Redeemer")
win.bgcolor("blue")
win.setup(width=800,height=600)
win.tracer(0)  #Stops the window from updating.Speeds up game

#Stick A
stick_a=turtle.Turtle()
stick_a.speed(0) # Speed of animation set to maximum possible speed
stick_a.shape("square")
stick_a.color("white")
stick_a.penup() # Not draw a line when moving
stick_a.shapesize(stretch_wid=5,stretch_len=1)
stick_a.goto(-370,0)

#Stick B
stick_b=turtle.Turtle()
stick_b.speed(0) # Speed of animation set to maximum possible speed
stick_b.shape("square")
stick_b.color("white")
stick_b.penup() # Not draw a line when moving
stick_b.shapesize(stretch_wid=5,stretch_len=1)
stick_b.goto(370,0)

#Ball
ball=turtle.Turtle()
ball.speed(0) # Speed of animation set to maximum possible speed
ball.shape("circle")
ball.color("white")
ball.penup() # Not draw a line when moving
ball.goto(0,0)
ball.dx=-0.1
ball.dy=0.1

#Creating the Score board
score_a=0
score_b=0
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,270)
pen.write(f"Player A :{score_a}  Player B :{score_b}",align="center",font=("Arial",20,"bold"))


#Functions
def up_a():
    y=stick_a.ycor()
    y+=20
    stick_a.sety(y)
#keyborad binding
win.listen()
win.onkeypress(up_a,"w")

def down_a():
    y=stick_a.ycor()
    y-=20
    stick_a.sety(y)

win.listen()
win.onkeypress(down_a,"s")

def up_b():
    y=stick_b.ycor()
    y+=20
    stick_b.sety(y)
#keyborad binding
win.listen()
win.onkeypress(up_b,"Up")

def down_b():
    y=stick_b.ycor()
    y-=20
    stick_b.sety(y)

win.listen()
win.onkeypress(down_b,"Down")

#Main game loop
while True:
    win.update()


    #Moving the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #Border check
    if ball.ycor()> 290:
        ball.sety(290)
        ball.dy*=-1
    if ball.ycor()< -290:
        ball.sety(-290)
        ball.dy*=-1
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1
        score_b+=1
        pen.clear()
        pen.write("Player A : "+str(score_a)+" Player B : "+str(score_b),align="center",font=("Arial",20,"bold"))
    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx*=-1
        score_a+=1
        pen.clear()
        pen.write("Player A : "+str(score_a)+" Player B : "+str(score_b),align="center",font=("Arial",20,"bold"))

    #Bounce on the stick
    if (ball.xcor()>360 and ball.xcor()<370)and (ball.ycor()<stick_b.ycor()+20 and ball.ycor()>stick_b.ycor()-20):
        ball.setx(360)
        ball.dx*=-1
    if (ball.xcor()<-360 and ball.xcor()>-370)and (ball.ycor()<stick_a.ycor()+20 and ball.ycor()>stick_a.ycor()-20):
        ball.setx(-360)
        ball.dx*=-1
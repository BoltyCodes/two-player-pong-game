#library

import turtle 

#screen settings
sc=turtle.Screen()
sc.title("Pong Game")
sc.bgcolor("grey")
sc.setup(width=800,height=600)

#left paddle
lftpad=turtle.Turtle()
lftpad.speed(0)
lftpad.shape("square")
lftpad.color("black")
lftpad.shapesize(stretch_wid=6,stretch_len=2)
lftpad.penup()
lftpad.goto(-390,0)

#right paddle
rgtpad=turtle.Turtle()
rgtpad.speed(0)
rgtpad.shape("square")
rgtpad.color("black")
rgtpad.shapesize(stretch_wid=6,stretch_len=2)
rgtpad.penup()
rgtpad.goto(380,0)

#ball
ball=turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.goto(0,0)
ball.dx=5
ball.dy=-5

#initalize score
left_player=0
right_player=0

#display score
sketch=turtle.Turtle()
sketch.speed(0)
sketch.color("blue")
sketch.penup()
sketch.hideturtle()
sketch.goto(0,260)
sketch.write("left player:0 right player:0",align="center",font=("Comic Sans MS",18,"normal"))

def paddleAup():
  y=lftpad.ycor()
  y=y+20
  lftpad.sety(y)

def paddleAdown():
  y=lftpad.ycor()
  y=y-20
  lftpad.sety(y)

def paddleBdown():
  y=rgtpad.ycor()
  y=y-20
  rgtpad.sety(y)

def paddleBup():
  y=rgtpad.ycor()
  y=y+20
  rgtpad.sety(y)

#keybindings
sc.listen()
sc.onkeypress(paddleAup,"e")
sc.onkeypress(paddleBup,"Up")
sc.onkeypress(paddleAdown,"x")
sc.onkeypress(paddleBdown,"Down")

#Main function the game
while True:
  sc.update()
  ball.setx(ball.xcor()+ball.dx)
  ball.sety(ball.ycor()+ball.dx)
 
  #checking borders
  if ball.ycor()>280:
     ball.sety(280)
     ball.dy *=-1
  
  if ball.ycor()<-280:
    ball.sety(280)
    ball.dy *=-1

  if ball.xcor()>400:
    ball.goto(0,0)
    ball.dy *=-1
    left_player +=1
    sketch.clear()
    sketch.write("left_player : {} right_player : {}".format(left_player,right_player),align="center",font=("Courier", 18, "normal"))

  if ball.xcor()<-400:
    ball.goto(0,0)
    ball.dy*=-1
    right_player+=1
    sketch.clear()
    sketch.write("left_player : {} right_player : {}".format(left_player,right_player),align="center",font=("Courier", 18, "normal"))

  
  #paddle ball collision
  if (ball.xcor()>360 and ball.xcor()<370) and (ball.ycor()<rgtpad.ycor()+40 and ball.ycor()>rgtpad.ycor()-40):
    ball.setx(360)
    ball.dx *=-1

  if (ball.xcor()<-360 and ball.xcor()>-370) and (ball.ycor()<lftpad.ycor()+40 and ball.ycor()>lftpad.ycor()-40):
    ball.setx(360)
    ball.dx *=-1

#scoring system (HW)

# Importing modules from Turtle ,Time and other 'self-made' classes
from turtle import Screen
import time
from paddle import Paddle
from  ball import Ball
from scorecard import ScoreCard

score_1 = ScoreCard((-140,300))                     # creating a scorecard for left
score_2= ScoreCard((140,300))                       # creating a scorecard for right
screen = Screen()                                   #creating a screen
screen.screensize(600,600)      # setting screensize
screen.bgcolor("black")
screen.tracer(0)
screen.title("Pong")                                # setting title of screen


# creating left and right paddle at (0,-280) and (0,280)
paddle_l = Paddle()
paddle_l.set_positon(-280)
paddle_r = Paddle()
paddle_r.set_positon(280)
ball = Ball()

# Setting the screen to listen the keyboard button
screen.listen()
screen.onkeypress(paddle_l.move_up, "w")
screen.onkeypress(paddle_l.move_down, "s")
screen.onkeypress(paddle_r.move_up, "Up")
screen.onkeypress(paddle_r.move_down, "Down")

# Setting the game value to True to start running game

is_game_start = True
while is_game_start:

    screen.update()
    time.sleep(0.08)
    ball.move()

# for upper and lower walls
    if ball.ycor() > 300 or ball.ycor() < -290:
       ball.y_cor *= -1

# for both paddles
    if (ball.distance(paddle_l) < 50 or ball.distance(paddle_r)) < 50 and (ball.xcor() > 259 or ball.xcor() < -259):
        ball.x_cor *= -1
        # for adding score to score board
        if ball.distance(paddle_l) < 60 :
            score_1.refresh_score()
        else:
            score_2.refresh_score()
# to getting out from while loop when ball missed by the paddle
    elif ball.xcor() > 290 or ball.xcor() < -290:
        is_game_start = False
        screen.clear()
        score_1.game_over()
#Setting screen method to exit only when clicked on screen

screen.exitonclick()
from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(800,600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.mode("logo")
screen.tracer(0)


player1 = Paddle((350, 0))
player2 = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()


screen.listen()
screen.onkey(player1.move_up, "Up")
screen.onkey(player1.move_down, "Down")
screen.onkey(player2.move_up, "w")
screen.onkey(player2.move_down, "s")

MAX_POINTS = 10
Y_movement = [10, -10]

while score.score1 <  MAX_POINTS and score.score2 < MAX_POINTS:
    screen.update()
    sleep(0.05)

    ball.moving()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 320 and ball.distance(player1) < 50:
        ball.bounce_x()
    if ball.xcor() < -320 and ball.distance(player2) < 50:
        ball.bounce_x()

    if ball.xcor() < -380:
        ball.home()
        ball.bounce_x()
        ball.y_move = random.choice(Y_movement)
        ball.bounce_y()
        score.score_increase1()
    if ball.xcor() > 380:
        ball.home()
        ball.bounce_x()
        ball.y_move = random.choice(Y_movement)
        ball.bounce_y()
        score.score_increase2()


score.game_over()

screen.exitonclick()

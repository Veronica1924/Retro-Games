from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width = 600, height = 600)
screen.title("Snake Game")
screen.bgcolor("pale green")
screen.tracer(0)
game_on = True

sarpe = Snake()
mancare = Food()
scoreboard = Scoreboard()

screen.listen()
screen.update()
screen.onkey(sarpe.up, "Up")
screen.onkey(sarpe.down, "Down")
screen.onkey(sarpe.right, "Right")
screen.onkey(sarpe.left, "Left")


while game_on:
    screen.update()
    sleep(0.05)
    sarpe.move()

    if sarpe.head.distance(mancare) < 15:
        mancare.refresh()
        scoreboard.score_increase()
        sarpe.extend()

    if sarpe.head.xcor() > 290 or sarpe.head.xcor() < -290 or sarpe.head.ycor() > 290 or sarpe.head.ycor() < -290:
        game_on = False
        scoreboard.game_over()
    for s in sarpe.snake[1:]:
        if sarpe.head.distance(s) < 10:
            game_on = False
            scoreboard.game_over()



screen.exitonclick()
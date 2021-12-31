from turtle import Screen
from time import sleep
from frog import Frog
from cars import Cars
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("grey")
screen.tracer(0)

frog = Frog()
cars = Cars()
score = Scoreboard()



screen.listen()

screen.onkey(frog.move_forward, "Up")
screen.onkey(frog.move_backward, "Down")
screen.onkey(frog.move_right, "Right")
screen.onkey(frog.move_left, "Left")






game_on = True

while game_on:
    screen.update()
    sleep(0.08)
    cars.move()
    for car in cars.cars:
        if car.xcor() < -280:
            cars.again(car)
        if frog.ycor() == car.ycor() - 10 and frog.distance(car) < 20:
            score.game_over()
            game_on = False











screen.exitonclick()
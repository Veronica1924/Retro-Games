from turtle import Turtle

STARTING_POINTS = [(0,0), (-20,0), (-40,0)]
MOVING_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]



    def create_snake(self):
        for position in STARTING_POINTS:
            self.increase(position)

    def increase(self, position):
        tim = Turtle(shape="square")
        tim.color("dark green")
        tim.pu()
        tim.goto(position)
        self.snake.append(tim)

    def extend(self):
        self.increase(self.snake[-1].position())



    def move(self):
        for s in range(len(self.snake) - 1, 0, -1):
            x = self.snake[s - 1].xcor()
            y = self.snake[s - 1].ycor()
            self.snake[s].goto(x, y)
        self.snake[0].forward(MOVING_DISTANCE)
    def up(self):
        if self.head.heading() !=  DOWN:
            self.head.setheading(UP)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

from turtle import Turtle


MOVING_PAS = 20

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.setheading(90)
        self.shapesize(5, 1)
        self.color("white")
        self.pu()
        self.goto(position)

    def move_up(self):
        new_y = self.ycor() + 20
        new_x = self.xcor()
        self.goto(new_x, new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        new_x = self.xcor()
        self.goto(new_x, new_y)

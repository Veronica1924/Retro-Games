from turtle import Turtle



class Frog(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("spring green")
        self.pu()
        self.goto(0,-280)
        self.setheading(90)

    def move_forward(self):
        self.forward(20)
    def move_backward(self):
        self.backward(20)
    def move_right(self):
        new_x = self.xcor() + 10
        self.goto(new_x,self.ycor())
    def move_left(self):
        new_x = self.xcor() - 10
        self.goto(new_x,self.ycor())
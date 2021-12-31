from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.pu()
        self.color("dark red")
        self.shapesize(0.7,0.7)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x = random.randrange(-280, 280)
        y = random.randrange(-280, 280)
        super().goto(x, y)
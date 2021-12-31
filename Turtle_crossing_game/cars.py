from turtle import Turtle
import random


class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.columns = [-70, -40, -10, 20, 50, 80]
        self.colors = ["red", "blue", "orange","purple", "green", "yellow"]
        self.hideturtle()
        self.create()

    def create(self):
        for i in range(len(self.columns)):
            y = self.columns[i]
            car = Turtle(shape="square")
            car.shapesize(stretch_len=3)
            car.color(random.choice(self.colors))
            car.pu()
            self.cars.append(car)
            car.goto(280, y)

    def move(self):
        for car in self.cars:
            pas = random.randint(10,30)
            car.backward(pas)

    def again(self, car):
        new_x = car.xcor() * -1
        car.goto(new_x,car.ycor())
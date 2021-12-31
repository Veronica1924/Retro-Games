from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.goto(-40, 270)
        self.color("black")
        self.score = 0
        self.update()

    def update(self):
        self.write("Score: " + str(self.score), False, "center", ("Courier", 16, "bold"))

    def score_increase(self):
        self.clear()
        self.score += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", False, "center", ("Courier", 16, "bold"))
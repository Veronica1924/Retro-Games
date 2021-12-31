from turtle import Turtle



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.goto(-40, 270)
        self.color("white")
        self.score1 = 0
        self.score2 = 0
        self.update()

    def update(self):
        self.write("Player 2    " + str(self.score2) + " : " + str(self.score1) + "    Player 1", False, "center", ("Courier", 16, "bold"))

    def score_increase1(self):
        self.clear()
        self.score1 += 1
        self.update()
    def score_increase2(self):
        self.clear()
        self.score2 += 1
        self.update()
    def game_over(self):

        self.goto(0, 0)
        if self.score1 > self.score2:
           winner = "Player 1"
        else:
            winner = "Player 2"
        self.write("Game Over! The winner is: " + winner, False, "center", ("Courier", 16, "bold"))
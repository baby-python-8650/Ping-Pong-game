from turtle import Turtle

class ScoreCard(Turtle):
    def __init__(self,position):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(2, 7)
        self.goto(position)
        self.l_score = 0
        self.r_score = 0

        self.show_score()

    def show_score(self):
        self.write(f"SCORE = {self.score}", align="center", font=("Arial", 15, "bold"))

    def refresh_score(self):
        self.clear()
        self.score += 1
        self.show_score()

    def game_over(self):
        self.goto(0,0)
        self.color("red")

        self.write(f"GAME-OVER", align="center", font=("Arial", 60, "bold"))

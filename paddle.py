from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(5, 1)
        self.color("white")

    def set_positon(self, val):
        self.goto(val, 0)

    def move_up(self):
        if self.ycor() < 250:
            self.goto(self.xcor(), self.ycor() + 30)

    def move_down(self):
        if self.ycor() > -250 :
            self.goto(self.xcor(), self.ycor() - 30)

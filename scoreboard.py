from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_score()

    def update_score(self):
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def level1(self):
        self.level += 1
        self.clear()
        self.update_score()



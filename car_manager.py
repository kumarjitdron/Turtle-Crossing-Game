from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.penup()
        self.shape("square")
        self.width(40)
        self.shapesize(stretch_len=2)
        self.goto(280, random.randint(-230, 230))
        self.setheading(180)
        self.car_speed = STARTING_MOVE_DISTANCE

    def move(self):
        self.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT







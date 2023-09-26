import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

tim = Turtle()
tim.hideturtle()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
score = Scoreboard()
screen.listen()
screen.onkey(player.move_up, "Up")

count = 0
cars = []
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if count == 6:
        cars.append(CarManager())
        count = 0
    count += 1
    for i in cars:
        i.move()
        if i.xcor() < -320:
            cars.remove(i)
        if i.distance(player) < 20:
            tim.write("Game Over", align="center", font=("Courier", 24, "normal"))
            game_is_on = False
    if player.is_at_finish_line():
        score.level1()




screen.exitonclick()
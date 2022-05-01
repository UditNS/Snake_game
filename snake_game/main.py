from turtle import Screen, Turtle
from snake import Snake
from food import Food
from highscore import Scoreboard
import time
screen = Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(height= 800, width= 800)
x_cor = [(20, 0), (0, 0), (-20, 0)]

segment = []
screen.listen()
screen.tracer(0)

sna = Snake()
food = Food()
tim = Turtle()
score = Scoreboard()

tim.hideturtle()
tim.color("white")
screen.onkey(sna.forr, "Up")
screen.onkey(sna.back, "Down")
screen.onkey(sna.right, "Right")
screen.onkey(sna.left, "Left")

is_game_on = True

while is_game_on:
    time.sleep(0.1)
    sna.move()
    screen.update()
    score.update_scoreboard()

    # Detect collision with food using turtle distance function
    if sna.segment[0].distance(food) < 15:
        food.refresh()
        sna.extend()
        score.increase_score()

# Detect collision with wall
    if sna.segment[0].xcor() > 370 or sna.segment[0].xcor() < -380 or sna.segment[0].ycor() > 370 or sna.segment[0].ycor() < -370:
        score.reset()
        sna.reset()
        is_game_on = False
        if is_game_on == False:
            tim.hideturtle()
            tim.goto(0, 0)
            tim.write("Gameover", align="center", font=("Verdana", 22, "normal"))

    # Detect collision with tail.
    for segmen in sna.segment[1:]:
        if sna.segment_head.distance(segmen) < 10:
            is_game_on = False
            tim.hideturtle()
            tim.goto(0, 0)
            tim.write("Gameover", align="center", font=("Verdana", 22, "normal"))



screen.exitonclick()

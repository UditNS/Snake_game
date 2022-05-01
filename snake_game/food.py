from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        super().shape("circle")
        self.penup()
        self.shapesize(stretch_wid= 0.5, stretch_len= 0.5)
        super().color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-360, 360)
        random_y = random.randint(-360, 360)
        self.goto(random_x, random_y)






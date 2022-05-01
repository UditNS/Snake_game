from turtle import Turtle, Screen

screen = Screen()
X_COR = [(20, 0), (0, 0), (-20, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.segment_head = self.segment[0]

    def create_snake(self):
        for x in X_COR:
            self.add_segment(x)

    def add_segment(self, x):
        tim = Turtle()
        tim.shape("square")
        tim.color("white")
        tim.penup()
        tim.goto(x)
        self.segment.append(tim)


    def extend(self):
        # This will add a new segment after collision with food
        self.add_segment(self.segment[-1].position())

    def move(self):

        for seg in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg - 1].xcor()
            new_y = self.segment[seg - 1].ycor()
            self.segment[seg].goto(new_x, new_y)
        self.segment[0].forward(20)

    def forr(self):
        if self.segment[0].heading() != DOWN:
            self.segment[0].setheading(UP)

    def back(self):
        if self.segment[0].heading() != UP:
            self.segment[0].setheading(DOWN)

    def left(self):
        if self.segment[0].heading() != RIGHT:
            self.segment[0].setheading(LEFT)

    def right(self):
        if self.segment[0].heading() != LEFT:
            self.segment[0].setheading(RIGHT)

    def reset(self):
        for segs in self.segment:
            segs.goto(1000, 1000)
        self.segment.clear()
        self.create_snake()
        self.segment_head = self.segment[0]

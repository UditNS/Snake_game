from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as self.highest:
            self.z = self.highest.read()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 350)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Scoreboard: {self.score} Highscore: {self.z}", align="center", font=("Verdana", 22, "normal"))


    def reset(self):
        if self.score > int(self.z):
            self.z = self.score
            with open("data.txt", mode="w") as self.high:
                self.high.write(str(self.z))
        self.score = 0

    def increase_score(self):
        self.score +=1
        self.update_scoreboard()
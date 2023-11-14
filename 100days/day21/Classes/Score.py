from turtle import Turtle

class Score(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.color("yellow")
        self.penup()
        self.hideturtle()
        self.setposition(0, 275)
        self.outcome = 0
        self.writeScore()
    
    def writeScore(self):
        score_str = f"Score = {self.outcome}"
        self.write(score_str, False, align="center", font=('Arial', 14, 'normal'))

    def updateScore(self):
        self.clear()
        self.outcome += 1
        self.writeScore()
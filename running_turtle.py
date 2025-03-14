from turtle import Turtle
class Running_Turtle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("green")
        self.left(90)
        self.goto(0,-280)
    def move_up(self):
        new_y = self.ycor()+10
        self.goto(0,new_y)
    def move_down(self):
        new_y = self.ycor()-10
        self.goto(0,new_y)
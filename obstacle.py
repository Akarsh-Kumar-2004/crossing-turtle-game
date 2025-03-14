import turtle
import random
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

class Obstacle():
    
    def __init__(self):
        # super().__init__()
        self.all_obs = []
    def obs_carry(self):
        
        obs = turtle.Turtle()
        obs.penup()
        obs.shape("square")
        obs.pos = random.choice(range(-280,281,20))
        obs.color(random.choice(COLORS))
        obs.shapesize(1,2)
        obs.goto(260,obs.pos)
        self.all_obs.append(obs)
    def move(self):
        time.sleep(0.1)
        for o in self.all_obs:
            o.backward(5)
            
        #     x = o.xcor()-10
        # # print("Current X:", obs.xcor())
        #     o.goto(x,o.pos)
        
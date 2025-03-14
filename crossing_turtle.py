'''
2:42
1. screen wagera set karenge
2. turle class banayenge and goto use karke y -280 se user ka input leke through onkey +20 karte rahenge..aur ye sab while loop mein hoga
3. obstacle class banayenge jismein square shape denge and shapesize mein x=2,y=1 kar denge...color denge random
   and choice mein denge ek preset color ki list ke form mein
4.touch class banayenge aur usmein distance funtion use karke less than 20 karke check karenge...
5. then check karenge ki upar waali wall ko if touch kar diya toh yipee
6. score ek se incr. kar denge and turtle reset hojaayega 
7. if score increase hua toh speed badh jaayegi obstacles ki by using time class
8. ho toh gaye gadhe...ab kya jaan lega
2:48
'''
import turtle
from running_turtle import Running_Turtle
from obstacle import Obstacle
import random
screen  = turtle.Screen()
screen.bgcolor("black")
screen.setup(600,600)
screen.title("CROSSING TURTLE GAME")
screen.tracer(0)
running_turtle = Running_Turtle()
obstacle = Obstacle()




screen.listen()
screen.onkey(running_turtle.move_up,"w")
screen.onkey(running_turtle.move_down,"s")

# pos_list = list(range(-280, 281, 20))
game_is_on = True
while game_is_on:
    screen.update()
    screen.delay(0.1)
    obstacle.obs_carry()
    
    obstacle.move()
    










screen.exitonclick()
from turtle import Turtle , Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="which tutle will win the race ?,Enter the color of your turtle")
colors = ["red","yellow","blue", "green", "purple", "orange"]
all_turtles = []

y_position =[-70, -40, -10, 20, 50, 80]
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on =True
    
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()> 230:  
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You are the winner! You bet on {user_bet} and it was correct.")
            else:
                print(f"You are the loser! AS you didn't bet on {winning_color}. Better luck next time.")
        
        rand_distance =random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()

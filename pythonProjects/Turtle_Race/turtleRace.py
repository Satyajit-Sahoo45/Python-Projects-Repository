from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make Your Bet", prompt="which turtle will win the race? Enter the color: ")
# print(user_bet)

color = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            wining_color = turtle.pencolor()
            if wining_color == user_bet:
                print(f"you've won! The {wining_color} turtle color is the winner")
            else:
                print(f"you've lost! The {wining_color} turtle color is the winner")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
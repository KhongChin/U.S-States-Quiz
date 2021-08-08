import pandas
from turtle import Turtle, Screen

data = pandas.read_csv("50_states.csv")
image = "blank_states_img.gif"

screen = Screen()
state_turtle = Turtle()
image_turtle = Turtle()

screen.title("U.S. States Game")
screen.addshape(image)
image_turtle.shape(image)
state_turtle.hideturtle()
state_turtle.penup()

SCORE = 0
correct_guesses = []

while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{SCORE}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missed_state = [state for state in data["state"] if state not in correct_guesses]
        print(missed_state)
        break

    for state in data["state"]:
        if answer_state == state:
            SCORE += 1
            correct_guesses.append(answer_state.title())
            x = int(data.loc[data["state"] == state]["x"].values)
            y = int(data.loc[data["state"] == state]["y"].values)
            state_turtle.goto(x, y)
            state_turtle.write(state)



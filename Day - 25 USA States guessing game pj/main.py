import turtle
import pandas

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"

def game_over():
    t.goto(0, 0)
    t.write("GAME OVER", align=ALIGNMENT, font=FONT)

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "/python 100 days bootcamp/Github.git/Day - 25 USA States guessing game pj/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("/python 100 days bootcamp/Github.git/Day - 25 USA States guessing game pj/50_states.csv")
all_states = data.state.to_list()
guessed_states = []
lives = 3

t = turtle.Turtle()
t.hideturtle()
t.penup()

while len(guessed_states) < 50 and lives > 0:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct, {lives} Lives Remaining", prompt="What's another state's name?")
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    else:
        if answer_state in all_states:
            guessed_states.append(answer_state)
            state_data = data[data.state == answer_state]
            x = int(state_data.iloc[0].x)
            y = int(state_data.iloc[0].y)
            t.goto(x, y)
            t.write(answer_state, align="center", font=("Arial", 12, "normal"))
            t.penup()
            t.goto(x + 20, y)  # Move the turtle to a new position after writing the state name
        else:
            lives -= 1
            screen.title(f"{len(guessed_states)}/50 States Correct, {lives} Lives Remaining")
            if lives ==  0:
                game_over()

screen.exitonclick()

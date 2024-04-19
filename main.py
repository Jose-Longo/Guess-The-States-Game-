from turtle import Turtle, Screen
import pandas

#Set up the screen
screen = Screen()
screen.setup(width=725, height=491)
screen.title("U.S. States Game")
screen.bgpic("blank_states_img.gif")

guesses = 0
guessed_states = []

game_is_on = True

while game_is_on:
    answer_state = screen.textinput(title=f"{guesses}/50 States Correct", prompt="What's another state's name?")
    answer_state = answer_state.title()

    #Check if user decide to end the game
    if answer_state == "Exit":
        missing_states = [state for state in data.state if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        game_is_on = False

    #Read the CSV with the states and their position on the map
    data = pandas.read_csv("50_states.csv")

    #Check if the guess is among the 50 states and place it on screen
    for state in data.state:
        if state == answer_state and answer_state not in guessed_states:
            new_text = Turtle()
            new_text.penup()
            new_text.color("black")
            new_text.hideturtle()
            xcor = int(data[data.state == state].x.iloc[0])
            ycor = int(data[data.state == state].y.iloc[0])
            new_text.goto(xcor, ycor)
            new_text.write(f"{answer_state}", align="center", font=("Arial", 8, "normal"))
            guesses += 1
            guessed_states.append(answer_state)

            if len(guessed_states) == 50:
                game_is_on = False


#Create a file with the states the user didn't guess


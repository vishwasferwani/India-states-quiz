import turtle
import pandas
import time
screen = turtle.Screen()
screen.title("India States game")

image = "india_blank_states.gif"
turtle.bgpic(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)


states_data = pandas.read_csv("States.csv")
states_name = states_data["state"].to_list()
print(states_name)

# print(user_answer)

def game():
    score = 0
    while score<50:

        with open("score.txt") as file:
            score = int(file.read())
        user_answer = screen.textinput(f"score:{score}/30", "Enter states name")

        if user_answer.title() == "Exit":
            break

        if user_answer.title() in states_name:

            turtle.shape("circle")
            turtle.shapesize(0.1)
            turtle.penup()
            turtle.color("red")
            state_row = states_data[states_data.state == user_answer.title()]
            # xcor = int(state_row.x)
            # ycor = int(state_row.y)
            turtle.goto(int(state_row.x),int(state_row.y))
            turtle.write(user_answer)

            score +=1
            # print(states_data[states_data.state == user_answer.title()])
            with open("score.txt", mode="w") as file:
                file.write(f"{score}")
            # screen.textinput(f"score:{score}/50", "Enter states name")
        else:
            game()


score = 0
with open("score.txt", mode="w") as file:
    file.write(f"{score}")
game()
turtle.mainloop()






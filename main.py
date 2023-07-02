from random import *
from turtle import *
from time import *
from snake import Snake


# Setting up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

# Stopping the animation
screen.tracer(0)

# Creates snake Object
snake = Snake()

# Waiting for commands
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# Makes game go on
game_is_on = True
while game_is_on:
    snake.move()
    update()
    sleep(0.1)




exitonclick()
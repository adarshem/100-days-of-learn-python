import time
from turtle import Screen
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# new_segment = Turtle(shape="square")
# new_segment.left(90)

# Create the Snake object
snake = Snake()
food = Food()

# Listen for keypress
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect snake head collision with food
    if snake.head.distance(food) < 15:
        food.refresh_food()


screen.exitonclick()
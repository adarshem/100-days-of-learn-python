import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=1000, height=1000)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

new_segment = Turtle(shape="square")
new_segment.color("white")
new_segment.penup()
new_segment.goto(-300, 300)
new_segment.pendown()
new_segment.goto(300, 300)
new_segment.goto(300, -300)
new_segment.goto(-300, -300)
new_segment.goto(-300, 300)
new_segment.hideturtle()

# Create the Snake object
snake = Snake()
food = Food()
scoreboard = Scoreboard()

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
        snake.add_tail_segment()
        food.refresh_food()
        scoreboard.update_score()

    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
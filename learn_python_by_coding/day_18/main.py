import random
import turtle
import colorgram
from turtle import Turtle, Screen
from turtle_colors import  colors
# change the colormode so that we could use (r,g,b)
turtle.colormode(255)
# Instantiates the Turtle and Screen classes and creates objects for them
my_turtle = Turtle()
my_screen = Screen()

my_screen.setup(width=800, height=600)  # Set a larger window size
my_turtle.shape("arrow")  # Make sure the turtle is visible

# Draw shapes like square, pentagon, hexagon etc
def draw_shape(side_length, number_of_sides, color):
    side_angle = 360 / number_of_sides
    my_turtle.pencolor(color)
    while number_of_sides > 0:
        my_turtle.forward(side_length)
        my_turtle.right(side_angle)
        number_of_sides -= 1

# draw_shape(100, 3, "DeepPink4")
# draw_shape(100, 4, "DeepPink4")
# draw_shape(100, 5, "chartreuse4")
# draw_shape(100, 6, "blue")
# draw_shape(100, 7, "maroon1")


def random_color_gen():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color =  (r, g, b)
    return rand_color

def random_walk(number_of_walks, step_size):
    my_turtle.speed(10)
    my_turtle.pensize(15)
    while number_of_walks > 0:
        color = random_color_gen()
        my_turtle.fillcolor(color)
        my_turtle.pencolor(color)
        move_to = random.choice([my_turtle.forward, my_turtle.backward])
        move_to(step_size)
        rotate_to = random.choice([my_turtle.left, my_turtle.right])
        rotate_to(90)
        number_of_walks -= 1

#random_walk(1000, 20)

def draw_spirograph(step, speed):
    my_turtle.speed(speed)
    for i in range(0, 360, step):
        color = random_color_gen()
        my_turtle.fillcolor(color)
        my_turtle.pencolor(color)
        my_turtle.circle(100)
        my_turtle.right(step)

# draw_spirograph(5,20)

def hirst_painting():
    # Extract 6 colors from an image.
    # colors_from_painting = colorgram.extract('painting.png', 20)
    rgb_colors = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

    my_turtle.hideturtle()
    my_turtle.speed(20)
    my_turtle.penup()
    my_turtle.setheading(225)
    my_turtle.forward(300)
    my_turtle.setheading(0)
    row_number = 1

    for i in range(1,101):
        my_turtle.dot(20, random.choice(rgb_colors))
        my_turtle.forward(50)
        if i % 10 == 0:
            if row_number % 2 == 0:
                my_turtle.setheading(90)
                my_turtle.forward(50)
                my_turtle.setheading(0)
                my_turtle.forward(50)
            else:
                my_turtle.setheading(90)
                my_turtle.forward(50)
                my_turtle.setheading(180)
                my_turtle.forward(50)
            row_number += 1

hirst_painting()
# # Keep the window open
my_screen.mainloop()
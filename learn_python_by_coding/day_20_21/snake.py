from turtle import Turtle
from typing import List

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments: List[Turtle] = []
        self.create_snake()
        self.head = self.segments[0]
        self.length = 3

    def create_snake(self):
        for position in STARTING_POSITION:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.segments[seg_num].goto(self.segments[seg_num - 1].xcor(), self.segments[seg_num - 1].ycor())

        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def add_tail_segment(self):
        new_tail_segment = Turtle(shape="square")
        new_tail_segment.color("white")
        new_tail_segment.penup()
        new_tail_segment.goto(self.segments[self.length - 1].xcor(), self.segments[self.length - 1].ycor())
        self.segments.append(new_tail_segment)
        self.length += 1

    # detect collision

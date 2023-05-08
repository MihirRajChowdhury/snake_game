from turtle import Turtle, Screen
import time

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        screen = Screen()
        # x = 0
        for position in STARTING_POS:
            self.add_segment(position)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def add_segment(self,position):
        new_body = Turtle("square")
        new_body.penup()
        new_body.color("blue")
        new_body.goto(position)
        self.segments.append(new_body)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for body_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[body_num - 1].xcor()
            new_y = self.segments[body_num - 1].ycor()
            self.segments[body_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        heading = self.head.heading()
        if heading != DOWN:
            self.head.setheading(UP)

    def down(self):
        heading = self.head.heading()
        if heading != UP:
            self.head.setheading(DOWN)

    def right(self):
        heading = self.head.heading()
        if heading != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        heading = self.head.heading()
        if heading != RIGHT:
            self.head.setheading(LEFT)


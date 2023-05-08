from turtle import Turtle, Screen

screen = Screen()
tim = Turtle()
screen.listen()


def up():
    heading = tim.heading()
    if heading == 180:
        tim.setheading(heading - 90)
        tim.forward(100)
    elif heading == 0:
        tim.setheading(heading + 90)
        tim.forward(100)
    elif heading == 90:
        tim.forward(100)


def down():
    heading = tim.heading()
    if heading == 180:
        tim.setheading(heading + 90)
        tim.forward(100)
    elif heading == 0:
        tim.setheading(heading - 90)
        tim.forward(100)
    elif heading == 270:
        tim.forward(100)


def right():
    heading = tim.heading()
    if heading == 90:
        tim.setheading(heading - 90)
        tim.forward(100)
    elif heading == 270:
        tim.setheading(heading + 90)
        tim.forward(100)
    elif heading == 0:
        tim.forward(100)


def left():

    heading = tim.heading()
    if heading == 90:
        tim.setheading(heading + 90)
        tim.forward(100)
    elif heading == 270:
        tim.setheading(heading - 90)
        tim.forward(100)
    elif heading == 180:
        tim.forward(100)

screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")


screen.exitonclick()

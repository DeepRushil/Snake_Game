import time
import random
from turtle import Screen, Turtle

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Snake starting positions
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

# Create snake
for pos in starting_positions:
    segment = Turtle("square")
    segment.color("white")
    segment.penup()
    segment.goto(pos)
    segments.append(segment)

head = segments[0]

# Food
food = Turtle("circle")
food.color("red")
food.penup()
food.speed(0)
food.goto(random.randint(-280, 280), random.randint(-280, 280))

# Score
score = 0
scoreboard = Turtle()
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 260)
scoreboard.write(f"Score: {score}", align="center", font=("Arial", 16, "normal"))

# Movement functions
def up():
    if head.heading() != 270:
        head.setheading(90)

def down():
    if head.heading() != 90:
        head.setheading(270)

def left():
    if head.heading() != 0:
        head.setheading(180)

def right():
    if head.heading() != 180:
        head.setheading(0)

# Keyboard bindings
screen.listen()
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")

# Game loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    # Move snake
    for i in range(len(segments) - 1, 0, -1):
        new_x = segments[i - 1].xcor()
        new_y = segments[i - 1].ycor()
        segments[i].goto(new_x, new_y)

    head.forward(20)

    # Collision with food
    if head.distance(food) < 15:
        food.goto(random.randint(-280, 280), random.randint(-280, 280))

        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        segments.append(new_segment)

        score += 1
        scoreboard.clear()
        scoreboard.write(f"Score: {score}", align="center", font=("Arial", 16, "normal"))

    # Collision with wall
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        game_is_on = False
        scoreboard.goto(0, 0)
        scoreboard.write("GAME OVER", align="center", font=("Arial", 24, "bold"))

    # Collision with tail
    for segment in segments[1:]:
        if head.distance(segment) < 10:
            game_is_on = False
            scoreboard.goto(0, 0)
            scoreboard.write("GAME OVER", align="center", font=("Arial", 24, "bold"))

screen.exitonclick()

# MY EFFORT
# from turtle import Turtle, Screen
# from random import random, randint, uniform
#
#
# t = Turtle(shape="square",)
# f = Turtle(shape="square")
# t.color("red")
# f.color("green")
# screen = Screen()
# screen.setup(width=600, height=600)
# screen.title("My Snake Game")
# screen.bgcolor("black")
# t.shapesize(1,3)
#
# random_space_x = uniform(0, -300)
# random_space_y = uniform(0, -300)
#
#
# def food():
#     f.penup()
#     f.setposition(x=random_space_x, y = random_space_y)
#
# food()
#
# def forward():
#     t.penup()
#     run = True
#     while run:
#         if t.xcor() >= 300:
#             run = False
#             print("You hit a wall")
#             t.home()
#         else:
#             t.forward(90)
#
# def back():
#     t.penup()
#     run = True
#     while run:
#         if t.ycor() <= 300:
#             run = False
#             print("You hit a wall")
#             t.home()
#         else:
#             t.back(90)
#
# def up():
#     t.penup()
#     run = True
#     while run:
#         if t.xcor() >= 300:
#             run = False
#             print("You hit a wall")
#             t.home()
#         else:
#             t.left(90)
#             t.forward(90)
#
#
# def down():
#     t.penup()
#     run = True
#     while run:
#         if t.ycor() >= 300:
#             run = False
#             print("You hit a wall")
#             t.home()
#         else:
#             t.right(90)
#             t.forward(90)
#
# # def down():
# #     t.penup()
# #     t.right(90)
# #     run = True
# #     while run:
# #         if t.xcor() >= 200:
# #             run = False
# #             print("You hit a wall")
# #         else:
# #             t.forward(90)
#
#
# screen.listen()
# screen.onkey(key="d", fun=forward)
# screen.onkey(key="a", fun=back)
# screen.onkey(key="w", fun=up)
# screen.onkey(key="s", fun=down)
# screen.exitonclick()

# SOLUTION
from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

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

    # Detect collision with turtle
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()

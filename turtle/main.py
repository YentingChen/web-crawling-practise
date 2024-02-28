from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Scoreboard

screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("orange")
screen.title("my snake game")
screen.tracer(0)

scoreboard = Scoreboard()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")


game_is_on = True

while game_is_on:
    snake.move()
    screen.update()
    time.sleep(0.1)

    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.grow()
        scoreboard.increase_score()

    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
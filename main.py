from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong")
screen.tracer(0)  # control the animation(the paddles in the left& right on the screen

r_paddle = Paddle((350, 0))   # x = 350 -> in right side , y = 0-> in the middle
l_paddle = Paddle((-350, 0))  # x = -350 -> in right left , y = 0-> in the middle
ball = Ball()
scoreboard = Scoreboard()

# control the paddle - move them by press on one of this keys.
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)  # move_speed = 0.1
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:  # height is 600 and the ball is 20px -> (600/2) -20
        ball.bounce_y()
    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    # detect r_paddle misses
    if ball.xcor() > 380:  # width is 800 and ball is 20px -> (800/2) -20, right is positive
        ball.reset_position()  # the ball go to the original position- (0,0)
        scoreboard.l_point()
    # detect l_paddle misses
    if ball.xcor() < -380:   # width is 800 and ball is 20px -> (800/2) -20, left is negative
        ball.reset_position()   # the ball go to the original position- (0,0)
        scoreboard.r_point()

screen.exitonclick()
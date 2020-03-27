import turtle


def make_screen():
    wnd = turtle.Screen()
    wnd.title('Pong')
    wnd.bgcolor('black')
    wnd.setup(width=800, height=600)
    wnd.tracer(0)
    wnd.listen()
    return wnd


def make_element(pos=(0, 0), type=None):
    trt = turtle.Turtle()  # initially it will be positioned center
    trt.shape('square')
    trt.speed(0)
    trt.shapesize(stretch_wid=4, stretch_len=.1)
    trt.color('white')
    trt.penup()  # Dont draw the line
    trt.goto(pos)  # positioning to the left
    if type == 'ball':
        trt.shapesize(stretch_len=1, stretch_wid=1)
        trt.shape('circle')
        trt.dx = .06
        trt.dy = .06
    return trt


def play_game(wnd, left_bar, right_bar, ball):
    def move_bar(bar, direction):
        speed = 15

        def inner():
            if direction == 'up':
                bar.sety(bar.ycor()+speed)
            if direction == 'down':
                bar.sety(bar.ycor()-speed)
        return inner
    wnd.onkeypress(move_bar(right_bar, 'up'), 'Up')
    wnd.onkeypress(move_bar(left_bar, 'up'), 'w')
    wnd.onkeypress(move_bar(right_bar, 'down'), 'Down')
    wnd.onkeypress(move_bar(left_bar, 'down'), 's')


def move_ball(ball, left_bar, right_bar):
    # setting up the boundaries
    if ball.xcor() > 380:
        if (ball.ycor() < right_bar.ycor()+40) and (ball.ycor() > right_bar.ycor()-40):
            ball.setx(380)
            ball.dx *= -1
        else:
            ball.goto(0, 0)

    if ball.xcor() < -380:
        if (ball.ycor() < left_bar.ycor()+40) and (ball.ycor() > left_bar.ycor()-40):
            ball.setx(-380)
            ball.dx *= -1
        else:
            ball.goto(0, 0)

    if ball.ycor() > 300:
        ball.sety(300)
        ball.dy *= -1
    if ball.ycor() < -300:
        ball.sety(-300)
        ball.dy *= -1

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


if __name__ == "__main__":
    wnd = make_screen()
    left_bar = make_element(pos=(-390, 0))
    right_bar = make_element(pos=(385, 0))
    ball = make_element(type='ball')

    play_game(wnd, left_bar, right_bar, ball)

    while True:
        wnd.update()
        move_ball(ball, left_bar, right_bar)

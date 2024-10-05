import turtle


def draw_koch_snowflake(level):

    def koch_snowflake(t, length, level):
        if level == 0:
            t.forward(length)
        else:
            length /= 3.0
            koch_snowflake(t, length, level - 1)
            t.left(60)
            koch_snowflake(t, length, level - 1)
            t.right(120)
            koch_snowflake(t, length, level - 1)
            t.left(60)
            koch_snowflake(t, length, level - 1)

    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.title("Koch snowflak")

    t = turtle.Turtle()
    t.speed("fastest")

    t.penup()
    t.goto(-200, 100)
    t.pendown()

    for _ in range(3):
        koch_snowflake(t, 400, level)
        t.right(120)

    turtle.done()


if __name__ == "__main__":
    draw_koch_snowflake(2)

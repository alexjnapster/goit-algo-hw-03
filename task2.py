import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def koch_snowflake(t, order, size):
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)


def main():
    turtle.setup(800, 600)
    window = turtle.Screen()
    window.title("Сніжинка Коха")

    t = turtle.Turtle()
    t.speed(0)

    order = int(window.numinput("Рівень рекурсії", "Введіть рівень рекурсії:", 3, minval=0, maxval=6))

    t.penup()
    t.goto(-150, 90)
    t.pendown()

    koch_snowflake(t, order, 300)

    t.hideturtle()
    window.mainloop()


if __name__ == "__main__":
    main()

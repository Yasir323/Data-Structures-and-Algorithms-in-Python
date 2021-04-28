import turtle


def tree(branch_length, t):
    if branch_length > 5:
        t.forward(branch_length)
        t.right(20)
        tree(branch_length - 15, t)
        t.left(40)
        tree(branch_length - 15, t)
        t.right(20)
        t.backward(branch_length)


def main():
    t = turtle.Turtle()
    screen = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75, t)
    screen.exitonclick()


main()

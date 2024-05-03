import turtle

# Функция для рисования фрактального дерева
def fractal_tree(t, branch_len, angle):
    if branch_len > 5:
        t.forward(branch_len)
        new_len = branch_len * 0.7
        t.left(angle)
        fractal_tree(t, new_len, angle)
        t.right(2 * angle)
        fractal_tree(t, new_len, angle)
        t.left(angle)
        t.backward(branch_len)

# Настройки окна и черепахи
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")

tree_turtle = turtle.Turtle()
tree_turtle.hideturtle()
tree_turtle.speed(0)
tree_turtle.color("green")

# Начальная позиция для рисования
tree_turtle.left(90)
tree_turtle.penup()
tree_turtle.setpos(0, -250)
tree_turtle.pendown()

# Рисование фрактального дерева
fractal_tree(tree_turtle, 100, 30)

# Закрытие окна по клику
screen.exitonclick()


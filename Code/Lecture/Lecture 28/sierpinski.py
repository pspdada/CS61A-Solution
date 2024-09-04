import turtle


# 定义一个函数来绘制一个等边三角形
def draw_triangle(length):
    for _ in range(3):
        turtle.forward(length)
        turtle.left(120)


# 定义递归函数来绘制谢尔宾斯基三角形
def sierpinski(order, length):
    if order == 0:
        draw_triangle(length)
    else:
        # 递归调用绘制三个小三角形
        sierpinski(order - 1, length / 2)
        turtle.forward(length / 2)
        sierpinski(order - 1, length / 2)
        turtle.backward(length / 2)
        turtle.left(60)
        turtle.forward(length / 2)
        turtle.right(60)
        sierpinski(order - 1, length / 2)
        turtle.left(60)
        turtle.backward(length / 2)
        turtle.right(60)


# 设置 turtle
turtle.speed(0)  # 设置最快的绘图速度
turtle.penup()
turtle.goto(-200, 100)  # 移动起点位置
turtle.pendown()

# 调用递归函数绘制谢尔宾斯基三角形
sierpinski(4, 400)

# 完成绘制
turtle.hideturtle()
turtle.done()

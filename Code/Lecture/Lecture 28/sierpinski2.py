import turtle
from typing import Callable

# (define (repeat k fn)
#   (fn)
#   (if (> k 1) (repeat (- k 1) fn)))
# (define (tri fn)
#   (repeat 3 (lambda () (fn) (lt 120))))
# (define (sier d k)
#   (tri (lambda () (if (= d 1) (fd k) (leg d k)))))
# (define (leg d k)
#   (sier (- d 1) (/ k 2))
#   (penup) (fd k) (pendown))


# 定义一个函数来绘制一个等边三角形
def draw_triangle(func: Callable):
    for _ in range(3):
        func()
        turtle.left(120)


def leg(order, length):
    sierpinski(order - 1, length / 2)
    turtle.penup()
    turtle.forward(length / 2)
    turtle.pendown()


# 定义递归函数来绘制谢尔宾斯基三角形
def sierpinski(order: int, length: int):
    draw_triangle(lambda: turtle.forward(length) if order == 1 else leg(order, length))


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

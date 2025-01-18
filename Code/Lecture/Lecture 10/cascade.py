# Lecture 10: Tree Recursion
def cascade(n: int):
    """
    Print a cascade of numbers from n to 1.

    >>> cascade(1234)
    1234
    123
    12
    1
    12
    123
    1234
    """
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n // 10)
        print(n)


def cascade2(n: int):
    """
    Print a cascade of numbers from n to 1. 仅仅是 cascade 将 print 函数提前。

    >>> cascade(1234)
    1234
    123
    12
    1
    12
    123
    1234
    """
    print(n)
    if n >= 10:
        cascade2(n // 10)
        print(n)


cascade(1234)
print("*" * 20)
cascade2(1234)
print("*" * 20)


def inverse_cascade(n: int):
    """
    >>> inverse_cascade(1234)
    1
    12
    123
    1234
    123
    12
    1
    """
    # grow(1234)：grow(123)->grow(12)->grow(1)->grow(0)->print(1)->print(12)->print(123)
    grow(n)
    # print(1234)
    print(n)
    # shrink(1234)：print(123)->shrink(123)->print(12)->shrink(12)->print(1)->shrink(1)->print(0)
    shrink(n)


def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)


grow = lambda n: f_then_g(grow, print, n // 10)  # noqa
shrink = lambda n: f_then_g(print, shrink, n // 10)  # noqa

inverse_cascade(1234)

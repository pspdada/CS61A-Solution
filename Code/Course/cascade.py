def cascade(n: int):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n // 10)
        print(n)


def cascade2(n: int):
    print(n)
    if n >= 10:
        cascade2(n // 10)
        print(n)


cascade(1234)
print("*" * 20)
cascade2(1234)
print("*" * 20)


def inverse_cascade(n: int):
    # grow(1234) 会递归调用 grow(123)、grow(12)、grow(1)，然后依次打印 1、12、123
    grow(n)
    # 打印 1234
    print(n)
    # shrink(1234) 会依次打印 123、12、1，然后递归调用 shrink(123)、shrink(12)、shrink(1)
    shrink(n)


def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)


grow = lambda n: f_then_g(grow, print, n // 10)
shrink = lambda n: f_then_g(print, shrink, n // 10)

inverse_cascade(1234)

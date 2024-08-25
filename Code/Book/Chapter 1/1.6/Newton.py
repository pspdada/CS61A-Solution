def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess


def approx_eq(x, y, tolerance=1e-15):
    return abs(x - y) < tolerance


def newton_update(f, df):
    def update(x):
        return x - f(x) / df(x)

    return update


def find_zero(f, df):
    def near_zero(x):
        return approx_eq(f(x), 0)

    return improve(newton_update(f, df), near_zero)


def power(x, n):
    """返回 x * x * x * ... * x，n 个 x 相乘"""
    product, k = 1, 0
    while k < n:
        product, k = product * x, k + 1
    return product


# 找到 a 的 n 次方根，即 x^n - a = 0 的解
def nth_root_of_a(n, a):
    def f(x):
        return power(x, n) - a

    def df(x):
        return n * power(x, n - 1)

    return find_zero(f, df)


print(nth_root_of_a(2, 64))
print(nth_root_of_a(3, 63))

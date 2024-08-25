def average(x, y):
    return (x + y) / 2


def sqrt_update(x, a):
    return average(x, a / x)


def approx_eq(x, y, tolerance=1e-15):
    return abs(x - y) < tolerance


def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess


def sqrt(a):
    def sqrt_update(x):
        return average(x, a / x)

    def sqrt_close(x):
        return approx_eq(x * x, a)

    return improve(sqrt_update, sqrt_close)


print(sqrt(64))

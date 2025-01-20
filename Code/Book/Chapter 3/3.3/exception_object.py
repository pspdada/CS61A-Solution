from math import sqrt
from typing import Callable


class IterImproveError(Exception):
    def __init__(self, last_guess):
        self.last_guess = last_guess


def improve(update: Callable, done: Callable, guess=1, max_updates=1000):
    k = 0
    try:
        while not done(guess) and k < max_updates:
            guess = update(guess)
            k = k + 1
        return guess
    except ValueError:
        raise IterImproveError(guess)


def newton_update(f, df):
    def update(x):
        return x - f(x) / df(x)

    return update


def find_zero(f: Callable, df: Callable, guess=1):
    def done(x):
        return f(x) == 0

    try:
        return improve(newton_update(f, df), done, guess)
    except IterImproveError as e:
        return e.last_guess

f = lambda x: 2 * x * x + sqrt(x) # noqa
df = lambda x: 4 * x + 1 / (2 * sqrt(x)) # noqa

print(find_zero(f, df))

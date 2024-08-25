a = 1


def f(g):
    a = 2
    return lambda y: a * g(y)


res = f(lambda y: a + y)(a)
print(res)  # The result is 4

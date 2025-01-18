# Lecture 23: Efficiency
import functools


def count_frames(f):
    @functools.wraps(f)
    def counted(n):
        counted.open_count += 1
        if counted.open_count > counted.max_count:
            counted.max_count = counted.open_count
        result = f(n)
        counted.open_count -= 1

        return result

    counted.open_count = 0  # The number of frames currently open
    counted.max_count = 0  # The maximum number of frames open at any time
    return counted


@count_frames
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)


print(fib(8))  # 21
print(fib.open_count)  # 0
print(fib.max_count)  # 8

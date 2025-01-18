# Lecture 17: Generators
from typing import Generator


def count_partitions(n: int, m: int) -> int:
    """
    Count partitions. The partitions of n using parts up to m can be counted
    recursively as the sum of the partitions of n - m using parts up to m and
    the partitions of n using parts up to m - 1.
    >>> count_partitions(6, 4)
    9
    """
    if n == 0:
        return 1
    elif n < 0 or m == 0:
        return 0
    else:
        with_m = count_partitions(n - m, m)
        without_m = count_partitions(n, m - 1)
        return with_m + without_m


def list_partitions(n: int, m: int) -> list[list[int]]:
    """
    List partitions.
    >>> for p in list_partitions(6, 4): print(p)
    [2, 4]
    [1, 1, 4]
    [3, 3]
    [1, 2, 3]
    [1, 1, 1, 3]
    [2, 2, 2]
    [1, 1, 2, 2]
    [1, 1, 1, 1, 2]
    [1, 1, 1, 1, 1, 1]
    """
    if n < 0 or m == 0:
        return []
    else:
        exact_match = [[m]] if n == m else []
        with_m = [p + [m] for p in list_partitions(n - m, m)]
        without_m = list_partitions(n, m - 1)
        return exact_match + with_m + without_m


def partitions(n, m):
    """
    List partitions.
    >>> for p in partitions(6, 4): print(p)
    2 + 4
    1 + 1 + 4
    3 + 3
    1 + 2 + 3
    1 + 1 + 1 + 3
    2 + 2 + 2
    1 + 1 + 2 + 2
    1 + 1 + 1 + 1 + 2
    1 + 1 + 1 + 1 + 1 + 1
    """
    if n < 0 or m == 0:
        return []
    else:
        exact_match = [str(m)] if n == m else []
        with_m = [p + " + " + str(m) for p in partitions(n - m, m)]
        without_m = partitions(n, m - 1)
        return exact_match + with_m + without_m


def partitions_yield(n: int, m: int) -> Generator:
    """
    yield 用于在生成器函数中生成一个值，并暂停函数的执行，直到生成器的 __next__() 方法被调用；
    yield from 用于委托子生成器。它可以将子生成器中的所有值依次生成出来，就像它们是外层生成器的一部分。

    >>> for p in partitions_yield(6, 4): print(p)
    2 + 4
    1 + 1 + 4
    3 + 3
    1 + 2 + 3
    1 + 1 + 1 + 3
    2 + 2 + 2
    1 + 1 + 2 + 2
    1 + 1 + 1 + 1 + 2
    1 + 1 + 1 + 1 + 1 + 1
    """
    if n > 0 and m > 0:
        if n == m:
            yield str(m)
        for p in partitions(n - m, m):
            yield p + " + " + str(m)
        # Equal to: yield from partitions(n, m - 1)
        for p in partitions(n, m - 1):
            yield p


if __name__ == "__main__":
    import doctest

    doctest.testmod()

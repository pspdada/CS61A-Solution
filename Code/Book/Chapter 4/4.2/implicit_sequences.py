# 4.2 隐式序列


class Stream:
    """惰性计算的链表"""

    class empty:
        def __repr__(self):
            return "Stream.empty"

    empty = empty()

    def __init__(self, first, compute_rest=lambda: Stream.empty):
        assert callable(compute_rest), "compute_rest 必须为可调用"
        self.first = first
        self._compute_rest = compute_rest

    @property
    def rest(self):
        """返回 Stream 的其他部分（缓存部分），如果需要计算，则计算"""
        if self._compute_rest is not None:
            self._rest = self._compute_rest()
            self._compute_rest = None
        return self._rest

    def __repr__(self):
        return "Stream({0}, <...>)".format(repr(self.first))


def map_stream(fn, s: Stream):
    if s is Stream.empty:
        return s

    def compute_rest():
        return map_stream(fn, s.rest)

    return Stream(fn(s.first), compute_rest)


def filter_stream(fn, s: Stream):
    if s is Stream.empty:
        return s

    def compute_rest():
        return filter_stream(fn, s.rest)

    if fn(s.first):
        return Stream(s.first, compute_rest)
    else:
        return compute_rest()


def first_k_as_list(s, k):
    first_k = []
    while s is not Stream.empty and k > 0:
        first_k.append(s.first)
        s, k = s.rest, k - 1
    return first_k


def integer_stream(first: int):
    """
    >>> positives = integer_stream(1)
    >>> positives
    Stream(1, <...>)
    >>> positives.first
    1
    """

    def compute_rest():
        return integer_stream(first + 1)

    return Stream(first, compute_rest)


def primes(pos_stream: Stream):
    """
    返回一个包含所有素数的 Stream

    >>> prime_numbers = primes(integer_stream(2))
    >>> first_k_as_list(prime_numbers, 7)
    [2, 3, 5, 7, 11, 13, 17]
    """

    def not_divible(x):
        return x % pos_stream.first != 0

    def compute_rest():
        return primes(filter_stream(not_divible, pos_stream.rest))

    return Stream(pos_stream.first, compute_rest)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)

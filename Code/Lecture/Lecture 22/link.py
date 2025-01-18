# Lecture22: Composition
from typing import Callable


class Link:
    empty = ()

    def __init__(self, first: int, rest: "Link" = empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_repr = ", " + repr(self.rest)
        else:
            rest_repr = ""
        return "Link(" + repr(self.first) + rest_repr + ")"

    def __str__(self):
        string = "<"
        while self.rest is not Link.empty:
            string += str(self.first) + " "
            self = self.rest
        return string + str(self.first) + ">"


def square(x):
    return x * x


def odd(x):
    return x % 2 == 1


def range_link(start, end):
    """
    Return a Link containing consecutive integers from start to end.

    >>> range_link(3, 6)
    Link(3, Link(4, Link(5)))
    """
    if start >= end:
        return Link.empty
    return Link(start, range_link(start + 1, end))


def map_link(f, s):
    """
    Return a Link with the elements of s transformed by f.

    >>> s = range_link(3, 6)
    >>> map_link(square, s)
    Link(9, Link(16, Link(25)))
    """
    if s is Link.empty:
        return s
    return Link(f(s.first), map_link(f, s.rest))


def filter_link(f: Callable, s: Link) -> Link:
    """
    Return a Link with elements of s for which f(element) is true.

    >>> s = range_link(3, 8) # 3, 4, 5, 6, 7
    >>> map_link(square, filter_link(odd, s))
    Link(9, Link(25, Link(49)))
    """
    if s is Link.empty:
        return s
    rest = filter_link(f, s.rest)
    if f(s.first):
        return Link(s.first, rest)
    else:
        return rest


def add(s: Link, v: int) -> Link:
    """Add v to an ordered list s with no repeats, returning modified s.
    >>> s = Link(1, Link(3, Link(4, Link(7))))
    >>> add(s, 0)
    Link(0, Link(1, Link(3, Link(4, Link(7)))))
    >>> add(s, 4)
    Link(0, Link(1, Link(3, Link(4, Link(7)))))
    >>> add(s, 8)
    Link(0, Link(1, Link(3, Link(4, Link(7, Link(8))))))
    """
    if s.first > v:  # Add to the front
        s.first, s.rest = v, Link(s.first, s.rest)  # Remember to construct a new Link object!!!
    elif s.first < v and s.rest is Link.empty:  # Add to the end
        s.rest = Link(v)
    elif s.first < v:
        add(s.rest, v)
    return s


if __name__ == "__main__":
    import doctest

    doctest.testmod()

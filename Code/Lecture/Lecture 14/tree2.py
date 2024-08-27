from tree import *


numbers = tree(3, [tree(4), tree(5, [tree(6)])])

haste = tree("h", [tree("a", [tree("s"), tree("t")]), tree("e")])


def print_sums(t, so_far):
    so_far += label(t)
    if is_leaf(t):
        print(so_far)
    else:
        for b in branches(t):
            print_sums(b, so_far)


def count_paths(t, total) -> int:
    """Return the number of paths in t that sum to total.

    >>> t = tree(3,[tree(-1),tree(1,[tree(2,[tree(1)]),tree(3)]),tree(1,[tree(-1)])])
    >>> count_paths(t, 3)
    2
    >>> count_paths(t, 4)
    2
    >>> count_paths(t, 5)
    0
    >>> count_paths(t, 6)
    1
    >>> count_paths(t, 7)
    2
    """
    if label(t) == total:
        found = 1
    else:
        found = 0
    return found + sum([count_paths(b, total - label(t)) for b in branches(t)])

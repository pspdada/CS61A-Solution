# Lecture 14: Trees
from tree import branches, is_leaf, label, tree

numbers = tree(3, [tree(4), tree(5, [tree(6)])])
#   3
#  / \
# 4   5
#    /
#   6

haste = tree("h", [tree("a", [tree("s"), tree("t")]), tree("e")])
#   h
#  / \
# a   e
# |\
# s t


def print_sums(t, so_far) -> None:
    """Print all sums of labels in t with labels in so_far.

    >>> print_sums(numbers, 0)
    7
    14
    >>> print_sums(haste, "")
    has
    hat
    he
    """
    so_far += label(t)
    if is_leaf(t):
        print(so_far)
    else:
        for b in branches(t):
            print_sums(b, so_far)


# t = tree(3, [tree(-1), tree(1, [tree(2, [tree(1)]), tree(3)]), tree(1, [tree(-1)])])
#      3
#     /|\
#   -1 1 1
#     /|  \
#    2 3  -1
#   /
#   1
def count_paths(t, total: int) -> int:
    """ "
    Return the number of paths from the root to **any node** in tree t
    for which the labels along the path sum to total.

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
    value = label(t)
    if value == total:
        found = 1
    else:
        found = 0
    return found + sum([count_paths(b, total - value) for b in branches(t)])


def count_paths2(t, total: int) -> int:
    """ "
    Return the number of paths from the root to **any node** in tree t
    for which the labels along the path sum to total.

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
    paths_cnt = [0]

    def count_helper(t, so_far):
        so_far += label(t)
        if so_far == total:
            paths_cnt[0] += 1
        for b in branches(t):
            count_helper(b, so_far)

    count_helper(t, 0)
    return paths_cnt[0]


if __name__ == "__main__":
    import doctest

    doctest.testmod()

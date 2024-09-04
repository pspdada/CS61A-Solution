class Tree:
    """A tree is a label and a list of branches."""

    def __init__(self, label, branches=[]):
        for branch in branches:
            assert isinstance(branch, Tree)
        self.label = label
        self.branches: list[Tree] = branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return f'Tree({self.label}{branch_str})'

    def __str__(self):
        return '\n'.join(self.indented())

    def indented(self):
        lines = []
        for b in self.branches:
            for line in b.indented():
                lines.append('  ' + line)
        return [str(self.label)] + lines

    def is_leaf(self):
        return not self.branches


def fib_tree(n) -> Tree:
    """A Fibonacci tree."""
    if n == 0 or n == 1:
        return Tree(n)
    else:
        left = fib_tree(n - 2)
        right = fib_tree(n - 1)
        fib_n = left.label + right.label
        return Tree(fib_n, [left, right])


def leaves(t: Tree) -> list:
    """Return a list of leaf labels in Tree T."""
    if t.is_leaf():
        return [t.label]
    else:
        all_leaves = []
        for b in t.branches:
            all_leaves.extend(leaves(b))
        return all_leaves


def height(t: Tree) -> int:
    """Return the height of a tree"""
    if t.is_leaf():
        return 0
    else:
        return 1 + max([height(b) for b in t.branches])


def prune(t: Tree, n: int):
    """prune all sub-trees whose label is n."""
    t.branches = [b for b in t.branches if b.label != n]
    for b in t.branches:
        prune(b, n)

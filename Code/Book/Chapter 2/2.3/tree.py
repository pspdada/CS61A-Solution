def tree(root_label, branches=[]):
    for branch in branches:
        assert is_tree(branch), "分支必须是树"
    return [root_label] + list(branches)


def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


def is_leaf(tree):
    return not branches(tree)


def label(tree):
    return tree[0]


def branches(tree):
    return tree[1:]


def partition_tree(n, m):
    """返回将 n 分割成不超过 m 的若干正整数之和的分割树"""
    # 一旦分割后的 n = 0，说明已经完成分割，返回 True
    if n == 0:
        return tree(True)
    # 分割后的 n < 0 说明正整数之和已超过最初被分割的 n，不符合要求；m 递减至 0，不符合需要分割为正整数的要求
    elif n < 0 or m == 0:
        return tree(False)
    else:
        left = partition_tree(n - m, m)
        right = partition_tree(n, m - 1)
        return tree(m, [left, right])


def print_parts(tree, partition=[]):
    if is_leaf(tree):
        if label(tree):
            print(" + ".join(partition))
    else:
        left, right = branches(tree)
        m = str(label(tree))
        print_parts(left, partition + [m])  # 左边是用了 m，所以 partition 需要加上 m
        print_parts(right, partition)  # 右边没有用 m，partition 不需要加上 m


partition = partition_tree(2, 2)
print(partition)
print_parts(partition)



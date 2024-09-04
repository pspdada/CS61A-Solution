empty = "empty"


def is_link(s):
    """判断 s 是否为链表"""
    return s == empty or (len(s) == 2 and is_link(s[1]))


def link(first, rest):
    """用 first 和 rest 构建一个链表"""
    assert is_link(rest), " rest 必须是一个链表"
    return [first, rest]


def first(s):
    """返回链表 s 的第一个元素"""
    assert is_link(s), " first 只能用于链表"
    assert s != empty, "空链表没有第一个元素"
    return s[0]


def rest(s):
    """返回 s 的剩余元素"""
    assert is_link(s), " rest 只能用于链表"
    assert s != empty, "空链表没有剩余元素"
    return s[1]


def len_link(s):
    """返回链表 s 的长度"""
    length = 0
    while s != empty:
        s, length = rest(s), length + 1
    return length


def getitem_link(s, i):
    """返回链表 s 中索引为 i 的元素"""
    while i > 0:
        s, i = rest(s), i - 1
    return first(s)


def len_link_recursive(s):
    """返回链表 s 的长度"""
    if s == empty:
        return 0
    return 1 + len_link_recursive(rest(s))


def getitem_link_recursive(s, i):
    """返回链表 s 中索引为 i 的元素"""
    if i == 0:
        return first(s)
    return getitem_link_recursive(rest(s), i - 1)


four = link(1, link(2, link(3, link(4, empty))))


def extend_link(s, t):
    """返回一个在 s 链表的末尾连接 t 链表后的延长链表"""
    assert is_link(s) and is_link(t)
    if s == empty:
        return t
    else:
        return link(first(s), extend_link(rest(s), t))


extend_link(four, four)


def apply_to_all_link(f, s):
    """应用 f 到 s 中的每个元素"""
    assert is_link(s)
    if s == empty:
        return s
    else:
        return link(f(first(s)), apply_to_all_link(f, rest(s)))


apply_to_all_link(lambda x: x * x, four)


def keep_if_link(f, s):
    """返回 s 中 f(e) 为 True 的元素"""
    assert is_link(s)
    if s == empty:
        return s
    else:
        kept = keep_if_link(f, rest(s))
        if f(first(s)):
            return link(first(s), kept)
        else:
            return kept


keep = keep_if_link(lambda x: x % 2 == 0, four)


def join_link(s, separator):
    """返回由 separator 分隔的 s 中的所有元素组成的字符串"""
    if s == empty:
        return ""
    elif rest(s) == empty:
        return str(first(s))
    else:
        return str(first(s)) + separator + join_link(rest(s), separator)


join_link(four, ", ")

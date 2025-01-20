# 2.4.9 约束传递 (Propagating Constraints)
from operator import add, mul, sub, truediv
from typing import Callable


def make_ternary_constraint(a, b, c, ab: Callable, ca: Callable, cb: Callable):
    """
    实现一个通用的三元（三向）约束
    约束 ab(a,b)=c，ca(c,a)=b，cb(c,b)=a
    """

    def new_value():
        av, bv, cv = [connector["has_val"]() for connector in (a, b, c)]
        if av and bv:
            c["set_val"](constraint, ab(a["val"], b["val"]))
        elif av and cv:
            b["set_val"](constraint, ca(c["val"], a["val"]))
        elif bv and cv:
            a["set_val"](constraint, cb(c["val"], b["val"]))

    def forget_value():
        for connector in (a, b, c):
            connector["forget"](constraint)

    constraint = {"new_val": new_value, "forget": forget_value}
    for connector in (a, b, c):
        connector["connect"](constraint)
    return constraint


def adder(a, b, c):
    """约束 a+b=c"""
    return make_ternary_constraint(a, b, c, add, sub, sub)


def multiplier(a, b, c):
    """约束 a*b=c"""
    return make_ternary_constraint(a, b, c, mul, truediv, truediv)


def constant(connector, value):
    """常量赋值：常量也是一种约束，但它永远不会发送任何消息，因为它只涉及它在构造时设置的单个连接器"""
    constraint = {}
    connector["set_val"](constraint, value)
    return constraint


def connector(name: str | None = None):
    """
    限制条件之间的连接器。
    连接器也是字典，其中包含一组值，也包括有局部状态的响应函数。连接器必须跟踪 informant 变量，它提供了当前的值，以及它参与的 constraints 列表
    """
    informant = None
    constraints = []

    def set_value(source, value):
        nonlocal informant
        val = connector["val"]
        if val is None:
            informant, connector["val"] = source, value
            if name is not None:
                print(name, "=", value)
            inform_all_except(source, "new_val", constraints)
        else:
            if val != value:
                print("Contradiction detected:", val, "vs", value)

    def forget_value(source):
        nonlocal informant
        if informant == source:
            informant, connector["val"] = None, None
            if name is not None:
                print(name, "is forgotten")
            inform_all_except(source, "forget", constraints)

    connector = {
        "val": None,
        "set_val": set_value,
        "forget": forget_value,
        "has_val": lambda: connector["val"] is not None,
        "connect": lambda source: constraints.append(source),
    }
    return connector


def inform_all_except(source, message, constraints):
    """告知信息除了 source 外的所有约束条件"""
    for c in constraints:
        if c != source:
            c[message]()


def converter(c: dict, f: dict):
    """用约束条件连接 c 到 f，将摄氏度转换为华氏度."""
    u, v, w, x, y = [connector() for _ in range(5)]
    multiplier(c, w, u)
    multiplier(v, x, u)
    adder(v, y, f)
    constant(w, 9)
    constant(x, 5)
    constant(y, 32)


celsius = connector("Celsius")
fahrenheit = connector("Fahrenheit")


converter(celsius, fahrenheit)
celsius["set_val"]("user", 25)
print("-" * 20)
fahrenheit["set_val"]("user", 212)
print("-" * 20)
celsius["forget"]("user")
print("-" * 20)
fahrenheit["set_val"]("user", 212)

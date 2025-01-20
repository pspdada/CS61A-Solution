# 2.6 实现类和对象

# 2.6.1 实现对象
def bind_method(value, instance):
    """Return a bound method if value is callable, or value otherwise."""
    if callable(value):

        def method(*args):
            """第一个参数 self 将会被绑定为 instance 的值"""
            return value(instance, *args)

        return method
    else:
        return value


def make_instance(cls):
    """Return a new object instance, which is a dispatch dictionary."""

    def get_value(name):
        if name in attributes:
            return attributes[name]
        else:
            # 在 get 消息中，如果 name 没有出现在本地 attributes 字典中，则会在类中查找，
            # 如果从类中查找返回的值是一个函数，则这个函数必须被绑定到实例。
            value = cls["get"](name)
            return bind_method(value, instance)

    def set_value(name, value):
        attributes[name] = value

    attributes = {}  # 存储实例的属性
    instance = {"get": get_value, "set": set_value}
    return instance


# 2.6.2 实现类
def init_instance(cls, *args):
    """Return a new object with type cls, initialized with args."""
    instance = make_instance(cls)
    init = cls["get"]("__init__")
    if init:
        init(instance, *args)
    return instance


def make_class(attributes, base_class=None):
    """Return a new class, which is a dispatch dictionary."""

    def get_value(name):
        if name in attributes:
            return attributes[name]
        elif base_class is not None:
            return base_class["get"](name)

    def set_value(name, value):
        attributes[name] = value

    def new(*args):
        return init_instance(cls, *args)

    cls = {"get": get_value, "set": set_value, "new": new}
    return cls


# 2.6.3 使用已经实现的对象


def make_account_class():
    """Return the Account class, which has deposit and withdraw methods."""
    interest = 0.02

    def __init__(self, account_holder):
        self["set"]("holder", account_holder)
        self["set"]("balance", 0)

    def deposit(self, amount):
        """Increase the account balance by amount and return the new balance."""
        new_balance = self["get"]("balance") + amount
        self["set"]("balance", new_balance)
        return self["get"]("balance")

    def withdraw(self, amount):
        """Decrease the account balance by amount and return the new balance."""
        balance = self["get"]("balance")
        if amount > balance:
            return "Insufficient funds"
        self["set"]("balance", balance - amount)
        return self["get"]("balance")

    return make_class(locals())


Account = make_account_class()

kirk_account = Account["new"]("kirk")

print(
    kirk_account["get"]("holder"),
    "\n",
    kirk_account["get"]("balance"),
    "\n",
    kirk_account["get"]("deposit")(20),
    "\n",
    kirk_account["get"]("withdraw")(5),
)


# 继承
def make_checking_account_class():
    """Return the CheckingAccount class, which imposes a $1 withdrawal fee."""
    interest = 0.01
    withdraw_fee = 1

    def withdraw(self, amount):
        fee = self["get"]("withdraw_fee")
        return Account["get"]("withdraw")(self, amount + fee)

    return make_class(locals(), Account)

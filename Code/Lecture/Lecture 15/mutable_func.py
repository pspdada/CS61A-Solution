from typing import Callable


def make_withdraw_list(balance: int) -> Callable[[int], str | int]:
    """A mutable functional implementation of a withdraw function."""
    b = [balance]  # a list is mutable

    def withdraw(amount: int) -> str | int:
        if amount > b[0]:
            return "Insufficient funds"
        b[0] -= amount
        return b[0]

    return withdraw


withdraw = make_withdraw_list(100)

print(withdraw(5))
print(withdraw(20))
print(withdraw(100))
print(withdraw(10))

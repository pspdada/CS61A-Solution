from typing import Callable


def make_withdraw(balance: int) -> Callable:
    def withdraw(amount: int) -> None:
        nonlocal balance  # Necessary since we assign to balance in `balance = ...` in this function
        if amount > balance:
            return "Insufficient funds"
        balance = balance - amount
        print(f"Now balance is {balance}")

    return withdraw


wd = make_withdraw(12)
wd2 = wd
wd2(1)
wd(1)

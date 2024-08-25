def split(n):
    return n // 10, n % 10


# 递归求和
def sum_digits(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last


# 迭代求和
def sum_digits_iter(n):
    total = 0
    while n > 0:
        n, last = split(n)
        total = total + last
    return total


# 用 Luhn 算法计算信用卡号码的校验和
# 信用卡号码的校验和是一个数字，它可以通过一种简单的算法来计算。首先，从右到左选择信用卡号码的每一个数字。对于偶数位上的数字，将其乘以 2；
# 如果乘积大于 9，则将其个位数和十位数相加。对于奇数位上的数字，不做任何处理。然后，将所有数字相加，得到的和就是信用卡号码的校验和。
def luhn_sum(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return luhn_sum_double(all_but_last) + last


def luhn_sum_double(n):
    all_but_last, last = split(n)
    luhn_digit = sum_digits(2 * last)
    if n < 10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last) + luhn_digit


print(sum_digits(114514) == sum_digits_iter(114514))  # True

print(luhn_sum(114514))  # 22

# Write a Function that takes a Number n and then returns a randomly generated number having exactly n digits (not starting with zero)

import random

def n_digits(ndigits):
    min_num = 10 ** (ndigits - 1)
    max_num = (10 ** ndigits) - 1

    if ndigits == 1:
        min_num = 0

    return random.randint(min_num, max_num)

x = int(input("Enter the No. of Digits:"))

print(n_digits(x))

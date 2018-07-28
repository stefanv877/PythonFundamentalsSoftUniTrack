"""
2. Sign of Integer Number
Create a function that prints the sign of an integer number n.
"""


def number_sign_print(n):
    if n == 0:
        print(f"The number {n} is zero.")
    elif n < 0:
        print(f"The number {n} is negative.")
    else:
        print(f"The number {n} is positive.")


n = int(input())
number_sign_print(n)
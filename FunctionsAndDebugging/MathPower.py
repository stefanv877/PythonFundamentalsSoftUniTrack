"""
6. Math Power
Create a function that calculates and returns the value of a number raised to a given power.
"""


def math_pow(number, power):
    result = number
    counter = int(power)
    for i in range(1, counter):
        result *= number
    return result


number = float(input())
power = float(input())

result = math_pow(number, power)
print(result)
"""
8. Multiply Evens by Odds
Create a program that reads an integer number and multiplies the sum of all its even digits by the sum of all its
odd digits.
"""


def sum_even_numbers(even_list):
    result = 0
    for num in even_list:
        result += num
    return abs(result)


def sum_odd_numbers(odd_list):
    result = 0
    for num in odd_list:
        result += num
    return abs(result)


def multiply_even_by_odd_numbers(numbers):
    even_list = []
    odd_list = []
    numbers = str(numbers)
    for num in numbers:
        if int(num) % 2 == 0:
            even_list.append(int(num))
        else:
            odd_list.append(int(num))

    return sum_even_numbers(even_list) * sum_odd_numbers(odd_list)


numbers = abs(int(input()))

print(multiply_even_by_odd_numbers(numbers))
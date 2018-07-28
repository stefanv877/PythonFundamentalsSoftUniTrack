"""
10. Square Numbers
Read a list of integers and extract all square numbers from it and print them in descending order. A square number
is an integer which is the square of any integer. For example, 1, 4, 9, 16 are square numbers.
"""

import math


list_numbers = list(map(int, input().split(" ")))
list_sqrt = []

for number in list_numbers:
    if number > 0 and math.sqrt(number) == int(math.sqrt(number)):
        list_sqrt.append(number)

list_sqrt.sort(reverse=True)

for number in list_sqrt:
    print(number, end=" ")
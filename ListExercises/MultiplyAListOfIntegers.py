"""
2. Multiply a List of Integers
Write a program to read a list of integers, an integer p, multiply each item by p and print the resulting list.
"""

list_numbers = list(map(int, input().split(" ")))
multiplier = int(input())

for number in list_numbers:
    print(number * multiplier, end=" ")
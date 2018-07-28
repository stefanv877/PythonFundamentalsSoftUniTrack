"""
6. Odd Numbers at Odd Positions
Write a program to read a list of integers and find how many odd numbers at odd positions the list holds. If there
are no numbers, which match this criterion, do not print anything
"""

list_numbers = list(map(int, input().split(" ")))

list_length = len(list_numbers)

for index in range(1, list_length, 2):
    if list_numbers[index] % 2 != 0:
        print(f"Index {index} -> {list_numbers[index]}")
"""
5. Count of Odd Numbers in List
Write a program to read a list of integers and find how many odd items it holds.
"""

list_numbers = list(map(int, input().split(" ")))

odd_items_count = 0

for number in list_numbers:
    if number % 2 != 0:
        odd_items_count += 1

print(odd_items_count)
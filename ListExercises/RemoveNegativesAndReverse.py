"""
7. Remove Negatives and Reverse
Read a list of integers, remove all negative numbers from it and print the remaining items in reversed order. In case
of no items left in the list, print “empty”.
"""

try:
    list_numbers = list(map(int, input().split(" ")))
except ValueError:
    list_numbers = []

list_length = len(list_numbers)

for index in range(list_length - 1, -1, -1):
    if list_numbers[index] < 0:
        list_numbers.remove(list_numbers[index])

list_length = len(list_numbers)

if list_length > 0:
    list_numbers.reverse()
    for number in list_numbers:
        print(number, end=" ")
else:
    print("empty")
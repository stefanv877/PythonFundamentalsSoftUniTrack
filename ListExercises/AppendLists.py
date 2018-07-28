"""
8. Append Lists
Write a program to append several lists of numbers.
 Lists are separated by ‘|’.
 Values are separated by spaces (‘ ’, one or several)
 Order the lists from the last to the first, and their values from left to right.
"""

user_input = input().split("|")

list_numbers = []

for item in reversed(user_input):
    temp_list = item.split(" ")
    for token in temp_list:
        if token:
            list_numbers.append(token)

for number in list_numbers:
    print(number, end=" ")
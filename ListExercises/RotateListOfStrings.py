"""
4. Rotate List of Strings
Write a program to read a list of strings, rotate it to the right and print its rotated items.
"""

list_strings = input().split(" ")
word = list_strings.pop()
list_strings.insert(0, word)

for string in list_strings:
    print(string, end=" ")
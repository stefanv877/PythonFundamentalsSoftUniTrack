"""
1. Odd Occurrences
Write a program that extracts from a given sequence of words all elements that present in it odd number of times
(case-insensitive).

 Words are given in a single line, space separated.
 Print the result elements in lowercase, in their order of appearance.
"""


list_words = input().lower().split(" ")
list_odd_words = {}

for word in list_words:
    if list_odd_words.__contains__(word):
        list_odd_words[word] += 1
    else:
        list_odd_words[word] = 1

list_output = []

for item in list_odd_words:
    if list_odd_words[item] % 2 != 0:
        list_output.append(item)

print(", ".join(list_output))
"""
3. Letter Repetition
You will be given a single string, containing random ASCII character. Your task is to print every character, and how
many times it has been used in the string.
"""

user_input = list(input())
char_count = {}

for char in user_input:
    if char_count.__contains__(char):
        char_count[char] += 1
    else:
        char_count[char] = 1

for char in char_count:
    print(f"{char} -> {char_count[char]}")
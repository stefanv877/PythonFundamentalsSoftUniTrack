"""
2. Count Real Numbers
Read a list of real numbers and print them in ascending order along with their number of occurrences.
"""

list_numbers = list(map(float, input().lower().split(" ")))
count = {}

for number in list_numbers:
    if count.__contains__(number):
        count[number] += 1
    else:
        count[number] = 1

for item in sorted(count.keys()):
    print(f"{item} -> {count[item]} times")
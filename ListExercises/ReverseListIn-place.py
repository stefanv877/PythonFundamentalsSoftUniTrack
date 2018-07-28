"""
6. Reverse List In-place
Read a list of integers on the first line of the console. After that, reverse the list in-place (as in, don’t create a new
collection to hold the result, reverse it using only the original list). After you are done, print the reversed list on the
console.
Note: You are not allowed to iterate over the list backwards and just print it
"""

import math

numbers = list(map(int, input().split(" ")))

last = -1

for i in range(math.floor(len(numbers) / 2)):
    temp = numbers[last]
    numbers[last] = numbers[i]
    numbers[i] = temp
    last -= 1

for number in numbers:
    print(number, end=" ")
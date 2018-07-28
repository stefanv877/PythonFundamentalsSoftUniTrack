"""
5. Smallest Element in List
Read a list of integers on the first line of the console. After that, find the smallest item in the list and print it on the
console.
"""

numbers = list(map(int, input().split(" ")))

print(min(numbers))
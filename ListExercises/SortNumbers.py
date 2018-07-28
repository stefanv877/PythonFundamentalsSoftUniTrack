"""
9. Sort Numbers
Read a list of integers and sort them in ascending order. Print the output as shown in the examples below.
"""

list_numbers = list(map(int, input().split(" ")))

list_numbers.sort()

#list_str = " <= ".join(str(n) for n in list_numbers)
list_str = list(map(str, list_numbers))

print(" <= ".join(list_str))
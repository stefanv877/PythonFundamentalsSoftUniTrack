"""
1. Sum List Items
Write a program, which reads a list of integers, calculates its sum and prints it.
The input consists of a number n (the number of items) + n integers, each as a separate line.
"""

input_count = int(input())
list_numbers = []
for i in range(input_count):
    list_numbers.append(int(input()))

print(sum(list_numbers))
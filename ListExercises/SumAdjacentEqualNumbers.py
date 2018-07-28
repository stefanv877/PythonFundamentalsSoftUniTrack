"""
11. Sum Adjacent Equal Numbers
Write a program to sum all adjacent equal numbers in a list of decimal numbers, starting from left to right.
 After two numbers are summed, the obtained result could be equal to some of its neighbors and should be
summed as well (see the examples below).
 Always sum the leftmost two equal neighbors (if several couples of equal neighbors are available).
"""

numbers_as_string = input().split()
numbers = list(map(float, numbers_as_string))

while True:
    first = 0
    second = 0
    for index in range(len(numbers) - 1):
        if float(numbers[index]) == float(numbers[index + 1]):
            first = numbers[index]
            second = numbers[index + 1]
            numbers[index + 1] = first + second
            numbers.remove(numbers[index])
            break
    if first == 0 and second == 0:
        break

for number in numbers:
    print(number, end= " ")
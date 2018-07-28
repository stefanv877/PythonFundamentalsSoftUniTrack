"""
7. Sort List Using Bubble Sort*
Read a list of integers on the first line of the console. After that, sort the list, using the Bubble Sort algorithm.
"""

numbers = list(map(int, input().split(" ")))


def bubble_sort(numbers):
    ln = len(numbers)
    for i in range(ln):
        is_swapped = False
        for j in range(0, ln - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                is_swapped = True
        if is_swapped is False:
            break


bubble_sort(numbers)
for n in numbers:
    print(n, end=" ")


#def bubble_sort(numbers):
#    is_swapped = True
#    while is_swapped:
#        temp = None
#        for i in range(len(numbers) - 1):
#            if numbers[i] > numbers[i + 1]:
#                temp = numbers[i + 1]
#                numbers[i + 1] = numbers[i]
#                numbers[i] = temp
#        if temp is None:
#            is_swapped = False
#
#
#bubble_sort(numbers)
#for n in numbers:
#    print(n, end=" ")
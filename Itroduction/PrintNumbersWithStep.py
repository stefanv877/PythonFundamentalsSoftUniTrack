"""
5. Numbers with Step
Write a python program, which receives a start number, an end number and a step. Write a simple for loop, which
prints all the numbers from the start number to the end number, using the specified step. Print the numbers on
separate lines.
Use the range() function.
"""


start_index = int(input())
end_index = int(input())
step_index = int(input())

for i in range(start_index, end_index, step_index):
    print(i)
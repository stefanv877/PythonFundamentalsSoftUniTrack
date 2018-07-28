"""
3. Printing Triangle
Create a function for printing triangles as shown below:

3 -> 1
     1 2
     1 2 3
     1 2
     1

4 -> 1
     1 2
     1 2 3
     1 2 3 4
     1 2 3
     1 2
     1
"""


def triangle_print(n):
    for i in range(1, n + 1):
        print(*range(1, i))
    for j in range(n + 1, 0, -1):
        print(*range(1, j))


n = int(input())

triangle_print(n)
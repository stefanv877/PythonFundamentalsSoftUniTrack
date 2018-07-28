"""
Draw a Filled Square
Draw at the console a filled square of size n like in the example:

4 -> --------
     -\/\/\/-
     -\/\/\/-
     --------
"""


def square_draw(n):
    top_and_bottom_borders = "-" * n * 2
    middle_row_count = n - 2
    middle_row_start_and_end_sign = "-"
    middle_row_filler = "\/" * (n - 1)

    print(top_and_bottom_borders)
    for j in range(middle_row_count):
        print(middle_row_start_and_end_sign + middle_row_filler + middle_row_start_and_end_sign)
    print(top_and_bottom_borders)


n = int(input())

square_draw(n)
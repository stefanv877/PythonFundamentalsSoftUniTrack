"""
5. Calculate Triangle Area
Create a function that calculates and returns the area of a triangle by given base and height.
Use a general formatting with 12 digits after the decimal point (e.g. {area:.12g})
"""


def triangle_area(b, h):
    return ((b * h) / 2)


b = float(input())
h = float(input())

result = float(triangle_area(b, h))

print(f"{result:.12g}")
"""
7. Greater of Two Values
You are given two values of the same type as input. The values can be of type int, char of string. Create a function
that returns the greater of the two values.
"""


def int_compare(a, b):
    if a > b:
        return a
    else:
        return b


def str_compare(a, b):
    if a > b:
        return a
    else:
        return b


def char_compare(a, b):
    if ord(a) > ord(b):
        return a
    else:
        return b


def greater_of_two_values_print(input_type):
    if input_type == "int":
        a = int(input())
        b = int(input())
        print(int_compare(a, b))
    elif input_type == "char":
        a = input()
        b = input()
        print(char_compare(a, b))
    else:
        a = input()
        b = input()
        print(str_compare(a, b))


greater_of_two_values_print(input_type = input())
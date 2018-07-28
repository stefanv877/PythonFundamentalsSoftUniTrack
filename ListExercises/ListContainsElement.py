"""
4. List Contains Item
Read a list of integers on the first line of the console and an integer N from the second line of the console and print
whether the item is contained in the list. If it is, print “yes”, otherwise print “no”.
"""

numbers = list(map(int, input().split(" ")))
number_to_find = int(input())

if numbers.__contains__(number_to_find):
    print("yes")
else:
    print("no")
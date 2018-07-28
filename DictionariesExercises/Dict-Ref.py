"""
4. Dict-Ref
You have been tasked to create a referenced dictionary, or in other words a dictionary, which knows how to
reference itself.
You will be given several input lines, in one of the following formats:
 {name} = {value}
 {name} = {secondName}
The names will always be strings, and the values will always be integers.
In case you are given a name and a value, you must store the given name and its value. If the name already EXISTS,
you must CHANGE its value with the given one.
In case you are given a name and a second name, you must store the given name with the same value as the value
of the second name. If the given second name DOES NOT exist, you must IGNORE that input.
When you receive the command “end”, you must print all entries with their value, by order of input, in the
following format:
{entry} === {value}
"""

user_input = input()
data = {}

while user_input != "end":
    user_input = user_input.split(" = ")
    name = user_input[0]
    if user_input[1].isdigit():
        data[name] = int(user_input[1])
    else:
        second_name = user_input[1]
        if data.__contains__(second_name):
            data[name] = data[second_name]

    user_input = input()

for key in data:
    print(f"{key} === {data[key]}")
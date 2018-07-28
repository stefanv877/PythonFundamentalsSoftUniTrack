"""
3. Dict-Ref-Advanced
Remember the Dict-Ref Problem from the previous exercise? Well this one is an Advanced Version.
You will begin receiving input lines containing information in one of the following formats:
 {key} -&gt; {value 1, value 2, …, value n}
 {key} -&gt; {otherKey}
The keys will always be strings, and the values will always be integers, separated by a comma and a space.
If you are given a key and values, you must store the values to the given key. If the key already exists, you must add
the given values to the old ones.
If you are given a key and another key, you must copy the values of the other key to the first one. If the other key
does not exist, this input line must be IGNORED.
When you receive the command “end”, you must stop reading input lines, and you must print all keys with their
values, in the following format:
 {key} === {value1, value2, value3. . .}
"""

user_input = input()
data = {}

while user_input != "end":
    user_input = user_input.split(" -> ")
    name = user_input[0]

    if not user_input[1].isalpha() and not data.__contains__(name):
        data[name] = user_input[1]
    elif not user_input[1].isalpha() and data.__contains__(name):
        # list_to_append = list(map(int, user_input[1].split(", ")))
        data[name] += ', ' + user_input[1]
    else:
        second_name = user_input[1]
        if data.__contains__(second_name):
            data[name] = data[second_name]

    user_input = input()

for key, value in data.items():
    print(f"{key} === {str(value)}")
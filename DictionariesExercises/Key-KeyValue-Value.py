"""
1. Key-Key Value-Value
Write a program, which searches for a key and value inside of several key-value pairs.
Input
 On the first line, you will receive a key.
 On the second line, you will receive a value.
 On the third line, you will receive N.
 On the next N lines, you will receive strings in the following format:
“key =&gt; {value 1};{value 2};…{value X}”
After you receive N key -&gt; values pairs, your task is to go through them and print only the keys, which contain the
key and the values, which contain the value. Print them in the following format:
{key}:
-{value1}
-{value2}
…
-{valueN}
"""

key = input()
value = input()
input_length = int(input())
data = {}

list_separators = ["=>", ";"]

while input_length > 0:
    data_input = input()
    for separator in list_separators:
        data_input = data_input.replace(separator, " ")
    data_input = data_input.split()
    data_key = data_input[0]
    data[data_key] = []
    for i in range(1, len(data_input)):
        data_value = data_input[i]
        data[data_key].append(data_value)

    input_length -= 1

for keys in data:
    if key in keys:
        print(f"{keys}:")
        for item in data[keys]:
            if value in item:
                print(f"-{item}")
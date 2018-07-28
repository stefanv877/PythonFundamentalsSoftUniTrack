"""
You have been tasked to sort out a database full of information about employees. You will be given several input
lines containing information in one of the following formats:
 {name} -&gt; {age}
 {name} -&gt; {salary}
 {name} -&gt; {position}
As you see you have 2 parameters. There can be only 3 cases of input:
If the second parameter is an integer, you must store it as name and age.
If the second parameter is a floating-point number, you must store it as name and salary.
If the second parameter is a string, you must store it as name and position.
You must read input lines, then parse and store the information from them, until you receive the command
“filter base”. When you receive that command, the input sequence of employee information should end.
On the last line of input you will receive a string, which can either be “Age”, “Salary” or “Position”. Depending on
the case, you must print all entries which have been stored as name and age, name and salary, or name and
position.
In case, the given last line is “Age”, you must print every employee, stored with its age in the following format:
Name: {name1}
Age: {age1}
====================
Name: {name2}
. . .

In case, the given last line is “Salary”, you must print every employee, stored with its salary in the following format:
Name: {name1}
Salary: {salary1}
====================
Name: {name2}
. . .
In case, the given last line is “Position”, you must print every employee, stored with its position in the following
format:
Name: {name1}
Position: {position1}
====================
Name: {name2}
. . .
NOTE: Every entry is separated with the other, with a string of 20 character ‘=’.
There is NO particular order of printing – the data must be printed in order of input.
"""

input_commands = input()
data = {}
data_index = 1
data[data_index] = {}

while input_commands != "filter base":
    input_commands = input_commands.split(" -> ")
    name = input_commands[0]
    data[data_index]["Name"] = name
    age = None
    salary = None
    position = None

    if input_commands[1].isdigit():
        age = int(input_commands[1])
        data[data_index]["Age"] = age
        data_index += 1
        data[data_index] = {}
    elif input_commands[1].__contains__("."):
        try:
            salary = float(input_commands[1])
            data[data_index]["Salary"] = salary
            data_index += 1
            data[data_index] = {}
        except ValueError:
            position = input_commands[1]
            data[data_index]["Position"] = position
            data_index += 1
            data[data_index] = {}
    else:
        position = input_commands[1]
        data[data_index]["Position"] = position
        data_index += 1
        data[data_index] = {}

    input_commands = input()

input_print_commands = input()
if input_print_commands == "Age":
    for data_id, data_info in data.items():
        for key in data_info:
            if key.__contains__("Age"):
                print(f"Name: {data_info['Name']}")
                print(f"Age: {data_info['Age']}")
                print("=" * 20)
elif input_print_commands == "Position":
    for data_id, data_info in data.items():
        for key in data_info:
            if key.__contains__("Position"):
                print(f"Name: {data_info['Name']}")
                print(f"Position: {data_info['Position']}")
                print("=" * 20)
elif input_print_commands == "Salary":
    for data_id, data_info in data.items():
        for key in data_info:
            if key.__contains__("Salary"):
                print(f"Name: {data_info['Name']}")
                print(f"Salary: {data_info['Salary']}")
                print("=" * 20)
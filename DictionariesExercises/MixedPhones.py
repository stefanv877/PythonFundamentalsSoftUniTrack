"""
5. Mixed Phones
You will be given several phone entries, in the form of strings in format:
{firstElement} : {secondElement}
The first element is usually the person’s name, and the second one – his phone number. The phone number consists
ONLY of digits, while the person’s name can consist of any ASCII characters.
Sometimes the phone operator gets distracted by the Minesweeper she plays all day, and gives you first the phone,
and then the name. e.g. : 0888888888 : Pesho. You must store them correctly, even in those cases.
When you receive the command “Over”, you are to print all names you’ve stored with their phones. The names
must be printed in alphabetical order.
"""

user_input = input()
data = {}

while user_input != "Over":
    user_input = user_input.split(" : ")
    first = user_input[0]
    second = user_input[1]

    if first.isdigit():
        data[second] = first
    else:
        data[first] = second

    user_input = input()

for item in sorted(data):
    print(f"{item} -> {data[item]}")
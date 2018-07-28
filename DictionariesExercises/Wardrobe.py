"""
9. Wardrobe
You just bought a new wardrobe. The weird thing about it is that it came prepackaged with a big box of clothes (just
like those refrigerators, which ship with free beer inside them)! So, you’ll need to find something to wear.
Input
On the first line of the input, you will receive n – the number of lines of clothes, which came prepackaged for the
wardrobe.
On the next n lines, you will receive the clothes for each color in the format:
 “{color} -&gt; {item1},{item2},{item3}…”
If a color is added a second time, add all items from it and count the duplicates.
Finally, you will receive the color and item of the clothing, that you need to look for.
Output
Go through all the colors of the clothes and print them in the following format:
{color} clothes:
* {item1} - {count}
* {item2} - {count}
* {item3} - {count}
…
* {itemN} - {count}
If the color lines up with the clothing item, print “(found!)” alongside the item. See the examples to better
understand the output.
"""

import re


number_input_lines = int(input())
wardrobe = {}

while number_input_lines > 0:
    clothe_data = input()
    clothe_data = re.split("; |-> |,", clothe_data)
    clothe_color = clothe_data[0].strip()
    if wardrobe.__contains__(clothe_color):
        pass
    else:
        wardrobe[clothe_color] = {}
    clothe_type = ""
    clothe_data_length = len(clothe_data)
    for index in range(1, clothe_data_length):
        clothe_type = clothe_data[index]
        if wardrobe[clothe_color].__contains__(clothe_type):
            wardrobe[clothe_color][clothe_type] += 1
        else:
            wardrobe[clothe_color][clothe_type] = 1

    number_input_lines -= 1

find_command = input().split(" ")
color_to_find = find_command[0]
type_to_find = find_command[1]

for color in wardrobe:
    print(f"{color} clothes:")
    for clothe in wardrobe[color]:
        if color_to_find == color and type_to_find == clothe:
            print(f"* {clothe} - {wardrobe[color][clothe]} (found!)")
        else:
            print(f"* {clothe} - {wardrobe[color][clothe]}")
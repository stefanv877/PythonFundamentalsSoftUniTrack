"""
10. Shellbound
Vladi is a crab. Crabs are scared of almost anything, which is why they usually hide in their shells. Vladi is a rich crab
though. He has acquired many outer shells, in different regions, in which he can hide – each with a different size.
However, it is really annoying to look after all your shells when they are so spread out. That is why Vladi decided to
merge all shells in each region, so that he has one big shell for every region. He needs your help to do that.
You will be given several input lines containing a string and an integer, separated by a space. The string will
represent the region’s name, and the integer – the shell in the given region, size.
You must store all shells in their corresponding regions.
If the region already exists, add the new shell to it. Make sure you have NO duplicate shells (shells with same size).
Vladi doesn’t like shells to have the same size.
When you receive the command “Aggregate”, you must stop reading input lines, and you must print every region,
all of the shells in that region, and the size of the giant shell after you’ve merged them in the following format:
{regionName} -&gt; {shell 1, shell 2…, shell n…} ({giantShell})
The giant shell size is calculated when you subtract the average of the shells from the sum of the shells.
Or in other words: (sum of shells) – ((sum of shells) / (count of shells)).
Constraints
 All numeric data will be represented with integer variables in range [0…1.000.000.000].
"""
import math


shell_input = input()
shell_data = {}

while shell_input != "Aggregate":
    shell_input = shell_input.split(" ")
    region = shell_input[0]
    size = int(shell_input[1])

    if shell_data.__contains__(region):
        if shell_data[region].__contains__(size):
            pass
        else:
            shell_data[region].append(size)
    else:
        shell_data[region] = []
        shell_data[region].append(size)

    shell_input = input()

for region in shell_data:
    aggregate_formula = math.ceil(sum(shell_data[region]) - (sum(shell_data[region]) / len(shell_data[region])))
    print(f"{region} -> {', '.join(str(x) for x in shell_data[region])} ({aggregate_formula})")
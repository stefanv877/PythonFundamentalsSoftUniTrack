"""
3. Count Numbers
Read a list of integers in range [0…1000] and print them in ascending order along with their number of
occurrences.
"""

numbers = sorted(list(map(int, input().split(" "))))

count = 1
for i in range(0, len(numbers)):
    if i < len(numbers) - 1:
        if numbers[i] == numbers[i + 1]:
            count += 1
        else:
            print(f"{numbers[i]} -> {count}")
            count = 1
    else:
        print(f"{numbers[i]} -> {count}")
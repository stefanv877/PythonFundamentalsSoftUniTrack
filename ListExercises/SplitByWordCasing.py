"""
2. Split by Word Casing
Read a text, split it into words and distribute them into 3 lists.
 Lower-case words like “programming”, “at” and “databases” – consist of lowercase letters only.
 Upper-case words like “PHP”, “JS” and “SQL” – consist of uppercase letters only.
 Mixed-case words like “C#”, “SoftUni” and “Java” – all others.
Use the following separators between the words: , ; : . ! ( ) " ' \ / [ ] space
Print the 3 lists as shown in the example below.
"""

words = input()

list_separators = [",", ";", ":", ".", "!", "(", ")", "\"", "\'", "\\", "/", "[", "]"]
for separator in list_separators:
    words = words.replace(separator, " ")

lower_case_list = []
mixed_case_list = []
upper_case_list = []

for word in words.split():
    if word.islower() and word.isalnum():
        lower_case_list.append(word)
    elif word.isupper() and word.isalnum():
        upper_case_list.append(word)
    else:
        mixed_case_list.append(word)

print(f"Lower-case: {', '.join(lower_case_list)}")
print(f"Mixed-case: {', '.join(mixed_case_list)}")
print(f"Upper-case: {', '.join(upper_case_list)}")

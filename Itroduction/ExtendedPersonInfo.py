"""
3. Extended Person Info
Write a Python program, which reads information about a person in the same format as the previous problem, and
prints it back to the console with the following format:
Name: {name}
Age: {age}
Town: {town}
Salary: ${salary}
Age range: {ageRange}
Salary range: {salaryRange}
Format the salary to the 2 nd decimal point.
The age range is as follows:
 If the person is less than 18 years old, they are a “teen”
 If the person is less than 70 years old, they are an “adult”
 Otherwise, the person is an “elder”
The salary range is as follows:
 If the salary is less than $500, it is “low”
 If the salary is less than $2000, it is “medium”
 Otherwise, the salary is “high”
"""


def range_of_age(age):
    if age < 18:
        return "teen"
    elif age > 18 and age < 70:
        return "adult"
    else:
        return "elder"

def range_of_salary(salary):
    if salary < 500:
        return "low"
    elif salary > 500 and salary < 2000:
        return "medium"
    else:
        return "high"

name = input()
age = int(input())
town = input()
salary = float(input())
age_range = range_of_age(age)
salary_range = range_of_salary(salary)

print(f"Name: {name}\n"
      f"Age: {age}\n"
      f"Town: {town}\n"
      f"Salary: ${salary:.2f}\n"
      f"Age range: {age_range}\n"
      f"Salary range: {salary_range}")
"""
7. User Logins
Write a program that receives a list of username-password pairs in the format “{username} -&gt; {password}”. If
there’s already a user with that username, replace their password. After you receive the command “login”, login
requests start coming in, using the same format. Your task is to print the status of user login, using different
messages as per the conditions below:
 If the password matches with the user’s password, print “{username}: logged in successfully”.
 If the user doesn’t exist, or the password doesn’t match the user, print “{username}: login failed”.
When you receive the command “end”, print the count of unsuccessful login attempts, using the format
“unsuccessful login attempts: {count}”.
"""

user_input = input()
data = {}

while user_input != "login":
    user_input = user_input.split(" -> ")
    name = user_input[0]
    password = user_input[1]

    data[name] = password

    user_input = input()

user_input = input()
unsuccessful_login_attempts = 0

while user_input != "end":
    user_input = user_input.split(" -> ")
    name = user_input[0]
    password = user_input[1]

    if data.__contains__(name) and data[name] == password:
        print(f"{name}: logged in successfully")
    else:
        print(f"{name}: login failed")
        unsuccessful_login_attempts +=1

    user_input = input()

print(f"unsuccessful login attempts: {unsuccessful_login_attempts}")
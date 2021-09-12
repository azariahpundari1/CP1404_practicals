# 1. Basic list operations
numbers = []
for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)
print("First number is ", numbers[0])
print("Last number is ", numbers[-1])
print("Minimum number is ", min(numbers))
print("Maximum number is ", max(numbers))
print("Sum of the numbers is ", sum(numbers)/len(numbers))

# 2. Woefully inadequate security checker

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Username: ")
while username not in usernames:
    print("Invalid Username")
    username = input("Username: ")
print("correct! ")

"""
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""
MENU = "(H) Display Hello\n(G) Display Goodbye\n(Q) Quit simulation"
name = input("What is your name: ").title()
print(MENU)
choice = input("Choice: ").upper()
while choice != 'Q':
    if choice == 'H':
        print("hello", name)
    elif choice == 'G':
        print("goodbye", name)
    else:
        print("Invalid input")
    print(MENU)
    choice = input("Choice: ").upper()
print("You have exited the simulation, congrats soldier")
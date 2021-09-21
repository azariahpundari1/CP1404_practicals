from prac_06.programming_language import ProgrammingLanguage

# because it said to create a basic program
name = input("Name: ")
year_of_birth = int(input("Year of birth: "))
if year_of_birth >= 1946 and year_of_birth <= 1964:
    print("Your name is {} and you're considered a baby boomer".format(name))
elif year_of_birth >= 1981 and year_of_birth <= 1996:
    print("Your name is {} and you're considered a millennial baby".format(name))
elif year_of_birth >= 1997 and year_of_birth <= 2015:
    print("Your name is {} and you're considered a generation z baby".format(name))
else:
    print("Your name is {} and your a baby".format(name))


ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

languages = [ruby, python, visual_basic]
print("The dynamically typed languages are:")
for language in languages:
    if language.is_dynamic():
        print(language.field)

# dont know what the __str__ is used for so i added this
for string in languages:
    print(string)

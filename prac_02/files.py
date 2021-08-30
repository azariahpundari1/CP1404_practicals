# 1
# get_name = input("Name: ")
# out_file = open("name.txt", 'w')
# print(get_name, file=out_file)
# out_file.close()

# 2
# in_file = open("name.txt", 'r')
# name = in_file.read()
# print(name)
# in_file.close()

# 3
number_file = open("numbers.txt", 'r')
number_one = int(number_file.readline())
number_two = int(number_file.readline())
addition = number_one + number_two
print(addition)
number_file.close()
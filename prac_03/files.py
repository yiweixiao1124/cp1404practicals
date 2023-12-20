# 1
name = input("Enter name: ").capitalize()
out_file = open("name.txt", 'w')
print(name, file=out_file)
out_file.close()
print()
# 2
in_file = open("name.txt", 'r')
name = in_file.readline()
print(f"Your name is {name}")
in_file.close()
print()
# 3
total = 0
in_file = open("numbers.txt", 'r')
lines = in_file.readlines()
for number in range(0, 2):
    number = in_file.readline()
    total = total + int(number)
print(total)
in_file.close()
print()
# 4
total = 0
in_file = open("numbers.txt", 'r')
numbers = in_file.readline()
for number in numbers:
    total = total + 1
print(total)

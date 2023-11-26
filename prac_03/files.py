# 1
name = input("Enter name: ").capitalize()
out_file = open("name.txt", 'w')
out_file.write(name)
out_file.close()
print()
# 2
in_file = open("name.txt", 'r')
name = in_file.readline()
print(f"Your name is {name}")
in_file.close()
print()
# 3
in_file = open("numbers.txt", 'r')
lines = in_file.readlines()
number1 = int(lines[0])
number2 = int(lines[1])
print(number1 + number2)
in_file.close()
print()
# 4
in_file = open("numbers.txt", 'r')
line = 0
for i in in_file:
    line = line + 1
print(line)

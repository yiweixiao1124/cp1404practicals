import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1?
# A random integer between 5 and 20
# What was the smallest number you could have seen, what was the largest?
# Smallest number: 5; largest number: 20
#
# What did you see on line 2?
# 3 or 5 or 7 or 9
# What was the smallest number you could have seen, what was the largest?
# Smallest number: 3; largest number: 9
# Could line 2 have produced a 4?
# NO
#
# What did you see on line 3?
# A random float between  2.5 and 5.5
# What was the smallest number you could have seen, what was the largest?
# Smallest number: 2.503935082025447; largest number: 5.467196383314342
#
# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 100))

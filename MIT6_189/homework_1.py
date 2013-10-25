# Angel Gonzalez
# hello_world.py
# Oct 25, 2013

# Exercise 1.2 and 1.3
vertical = "  |  |  "
horizontal = "--------"

print vertical
print horizontal
print vertical
print horizontal
print vertical

# Exercise 1.4

print (3 * 5) / (2 + 3)
print ((7 + 9) ** (1 / 2.0)) * 2
print (4 - 7) ** 3
print (-19 + 100) ** (1 / 4.0)
print (6 % 4)

a = 4 * 2 ** 3
b = (4 * 2) ** 3

print a
print b

# Exercise 1.5

first_name = raw_input("Enter your first name: ")
last_name = raw_input("Enter your last name: ")
date_birth = input("Enter your date of birth: ")
month_birth = raw_input("Month? ")
year_birth = input("Year? ")
print "%s %s was born on %s %d, %d" % (first_name, last_name, month_birth, date_birth, year_birth)

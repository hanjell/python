# Name: Angel Gonzalez
# Section: Week 1
# Date: Oct 25, 2013
# hw1.py

##### Template for Homework 1, exercises 1.2-1.5 ######

print "********** Exercise 1.2 **********"

print "  |  |  "
print "--------"
print "  |  |  "
print "--------"
print "  |  |  "

print "********** Exercise 1.3 **********"

vertical = "  |  |  "
horizontal = "--------"

print vertical
print horizontal
print vertical
print horizontal
print vertical

print "********** Exercise 1.4 **********"
print "********* Part II *************"

print (3 * 5) / (2 + 3)
print ((7 + 9) ** (1 / 2.0)) * 2
print (4 - 7) ** 3
print (-19 + 100) ** (1 / 4.0)
print (6 % 4)

print "********* Part III *************"

a = 4 * 2 ** 3
b = (4 * 2) ** 3

print a
print b

print "********** Exercise 1.5 **********"

first_name = raw_input("Enter your first name: ")
last_name = raw_input("Enter your last name: ")
date_birth = input("Enter your date of birth: ")
month_birth = raw_input("Month? ")
year_birth = input("Year? ")
print "%s %s was born on %s %d, %d" % (first_name, last_name, month_birth, date_birth, year_birth)
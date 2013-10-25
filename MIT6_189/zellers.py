# Angel Gonzalez
# hello_world.py
# Oct 25, 2013

date_birth = input("Enter your date of birth: ")
month_birth = input("Month? (1-12) ")
year_birth = input("Year? ")

if (month_birth < 3):
	year_birth -= 1

A = (month_birth - 2) % 12
B = date_birth
C = year_birth % 100
D = year_birth / 100

W = (13 * A - 1) / 5
X = C / 4
Y = D / 4
Z = W + X + Y + B + C - 2 * D
R = Z % 7

if R < 0:
	R += 7

print R
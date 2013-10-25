# Angel Gonzalez
# hello_world.py
# Oct 25, 2013

# 1
for x in xrange(2,10):
	print 1.0 / x

# 2
top = input("Enter a positive number: ")
if top >= 0:
	while top >= 0:
		print top
		top-=1
else:
	print "You entered a negative number"
	
# 3
base = input("Enter the base: ")
exp = input("Enter the exponent: ")
if exp < 0:
	print "Negative value entered"
else:
	exp_value = 1
	for x in xrange(0,exp):
		exp_value *= base

	print "Result: %f" % exp_value

# 4
while True:
	value = input("Enter a number divisible by 2: ")
	if (value % 2 == 0):
		print "Great! You entered a number divisible by 2."
		break;
	else:
		print "Ouch. You failed. Try again"
		
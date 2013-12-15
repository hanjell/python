# Name:
# Section:
# hw2.py

##### Template for Homework 2, exercises 2.0 - 2.5  ######
import math
import random

# **********  Exercise 2.0 ********** 

def f1(x):
    print x + 1

def f2(x):
    return x + 1

# **********  Exercise 2.1 ********** 

def rps(player1, player2):
	if player1 == player2:
		return "Tie"
	elif (player1 == "rock" and player2 == "scissors") or (player1 == "paper" and player2 == "rock") or (player1 == "scissors" and player2 == "paper"):
		return "Player1 wins."
	elif (player2 == "rock" and player1 == "scissors") or (player2 == "paper" and player1 == "rock") or (player2 == "scissors" and player1 == "paper"):
		return "Player2 wins."
	else:
		return "Not possible"
	

# Test Cases for Exercise 2.1

print "Round 1:"
print rps("rock", "scissors")

print "Round 2:"
print rps("paper", "scissors")

print "Round 3:"
print rps("paper", "paper")

# ********** Exercise 2.2 ********** 

def is_divisible(m, n):
	if (n == 0):
		return False
	return ((m % n) == 0)

# Test cases for is_divisible
## Provided for you... uncomment when you're done defining your function

print is_divisible(10, 5)  # This should return True
print is_divisible(18, 7)  # This should return False
print is_divisible(42, 0)  # What should this return?


# Define not_equal function here
def not_equal(x, y):
	return (x < y) or (x > y)

# Test cases for not_equal
print not_equal(1, 5)
print not_equal(-10, 0)
print not_equal(1, 1)

# ********** Exercise 2.3 ********** 

## 1 - multadd function
def multiadd(a, b, c):
	return (a * b) + c

## 2 - Equations
##### YOUR CODE HERE #####


# Test Cases
angle_test = multiadd(1.0/2.0, math.cos(math.pi / 4.0), math.sin(math.pi / 4.0))
print "sin(pi/4) + cos(pi/4)/2 is:"
print angle_test

ceiling_test = multiadd(2.0, math.log(12.0,7.0), math.ceil(276.0 / 19.0))
print "ceiling(276/19) + 2 log_7(12) is:"
print ceiling_test

## 3 - yikes function
def yikes(x):
	return multiadd(x, math.exp(-x), math.sqrt(1 - math.exp(-x)))


# Test Cases
x = 5
print "yikes(5) =", yikes(x)

# ********** Exercise 2.4 **********

## 1 - rand_divis_3 function
def rand_divis_3():
	a = random.randint(0, 100)
	print a
	return (a % 3 == 0)

# Test Cases
print rand_divis_3()
print rand_divis_3()
print rand_divis_3()

## 2 - roll_dice function - remember that a die's lowest number is 1;
                            #its highest is the number of sides it has
##### YOUR CODE HERE #####

# Test Cases
##### YOUR CODE HERE #####                            


# ********** Exercise 2.5 **********

# code for roots function
##### YOUR CODE HERE #####   

# Test Cases
##### YOUR CODE HERE #####   
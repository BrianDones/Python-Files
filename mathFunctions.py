#Author: Brian Dones
#Date: Dec 17, 2015


# Method that takes two numbers and add them together returning the result.
def add(a,b):
	return a+b
# Method that takes two numbers and subtracts them returning the result.
def subtract(a,b):
	return a-b
# Method that takes two numbers and returns the product of the two.
def multiply(a,b):
	return a*b
# Method that takes two numbers and divides the first number by the second number.
def divide(a,b):
	return a/b
# Method that takes a number and calculates the factorial of that number. Performed by doing a recursion.
def factorial(n):
	counter = 0
	if n<1 and counter == 0:
		return "Invalid Argument: Number must be greater than 0"
	elif n<2:
		return 1
	else:
		counter += 1
		total = n * factorial(n-1)
		return total

#test code for factorial command
# a = 5
# while (a > -2):
# 	print(factorial(a))
# 	a -= 1

# Method that takes a number and calculates the
def fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)

#test code for fib command
# a = 0
# while (a < 11):
# 	print(fib(a))
# 	a += 1

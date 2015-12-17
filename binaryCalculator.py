#Author: Brian Dones
#Date: Dec 17, 2015

# Method that takes a decimal number and converts the number to binary.
def decToBin(n):
	result = ""
	numOfBits = 0
	# First we find how many bits we will need to represent our binary number.
	while n >= pow(2,numOfBits):
		numOfBits += 1

	# After finding out how many bits we need to represent our binary number, figure out which bits are 1's and 0's
	while numOfBits > 0:
		# If the current value of n % 2^numberOfBits is greater than 0, we "enable" that bit appending a "1" to our binary string, set n to the result to keep the remainder value, and shift to the next column.
		if (n%pow(2,numOfBits-1) > 0 and n != n%pow(2,numOfBits-1)):
			n = n%pow(2,numOfBits-1)
			result += "1"
			numOfBits -= 1
		# If the current value of n is not 0 and the result of n % 2^numOfBits equals 0, we still are going to enable the bit and shift to the next column.
		elif (n != 0 and n%pow(2,numOfBits-1) == 0):
			n = n%pow(2,numOfBits-1)
			result += "1"
			numOfBits -= 1
		# If n = 0 or if n is less than 2^numOfBits, then we append a "0" to our binary string.
		else:
			result += "0"
			numOfBits -= 1

	return result

# Method that takes a binary string and converts the string into a decimal number.
def binToDec(binaryNumber):
	numOfBits = len(binaryNumber)
	index = 0
	num = 0

	# Iterate through the each index of the binary string
	for index in range (len(binaryNumber)):
		# If the bit is a 1, add the value to the current total and shift to the next index value.
		if binaryNumber[index] == "1":
			num += pow(2,numOfBits-1)
			numOfBits -= 1
		# If the bit is a 0, just shift to the next index value.
		else:
			numOfBits -= 1

	return num


################################################################################
################################################################################
################################################################################

# Prompts the user for a decimal number to convert to Binary.
# convertThis = input("Enter a decimal number to convert into Binary: ")
# print(decToBin(eval(convertThis)))

# # Prompts the user for a binary string to convert to a decimal number.
# convertThis = input("Enter a binary number to convert into Decimal: ")
# print(binToDec(convertThis))
print("############################################################")
print("#        Hello and welcome to My Binary Calculator!        #")
print("#                                                          #")
print("#                  Calculator Functions                    #")
print("# 1- Convert Decimal to Binary.                            #")
print("# 2- Convert Binary to Decimal.                            #")
print("# o- Show calculator functions.                            #")
print("# q- Exit Brian's Binary Calculator.                       #")
print("#                                                          #")
print("############################################################")


#TODO: be able to handle invalid input such as 1r or 1!
function = input("Please choose a function to perform: ")
while function != "q":
	if function == "1":
		convertThis = input("Enter a decimal number to convert to binary or q to exit to menu: ")
		if convertThis == "q":
			function = input("Please choose a function to perform: ")
		else:
			print(decToBin(eval(convertThis)))


#TODO: be able to handle invalid input such as 102
	elif function == "2":
		convertThis = input("Entery a binary number to convert to decimal or q to exit to menu: ")
		if convertThis == "q":
			function = input("Please choose a function to perform: ")
		else:
			print(binToDec(convertThis))




	elif function == "o" or "O":
		print("############################################################")
		print("#                  Calculator Functions                    #")
		print("# 1- Convert Decimal to Binary.                            #")
		print("# 2- Convert Binary to Decimal.                            #")
		print("# o- Show calculator functions.                            #")
		print("# q- Exit Brian's Binary Calculator.                       #")
		print("#                                                          #")
		print("############################################################")
		function = input("Please choose a function to perform: ")


	else:
		function = input("Invalid input: Please select a valid option or choose o to see options: ")

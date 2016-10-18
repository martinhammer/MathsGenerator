import random

# ------------------------------------------
# You can set the following parameters

# how many rows to generate
outputRows = 36 

# highest number for additions (both left and right)
maxSummand = 10

# highest number for subtraction left hand side (minuend)
maxMinuend = 20

# highest number for subtraction right hand side (subtrahend)
maxSubtrahend = 10

# maximum number of zeroes allowed to be generated (too many zeroes make the exercise too easy :))
maxZeros = 2

# ------------------------------------------
# No need to make changes below this line

# current number of zeros
countZeros = 0

def gimmeNumber( minValue, maxValue ):

	global maxZeros
	global countZeros

	randomNumber = random.randrange( minValue, maxValue )
	while ( randomNumber == 0 ) and ( countZeros >= maxZeros ):
		randomNumber = random.randrange( minValue, maxValue )

	return randomNumber

# ------------------------------------------

# main loop which generates random problems
for i in range( outputRows ):

	# randomly decide kind of problem to generate
	if random.randint( 0, 1 ) == 0:
		operand = '+'
	else:
		operand = '-'

	# generate numbers for an addition problem
	if operand == '+':

		left = gimmeNumber( 0, maxSummand )
		if left == 0: countZeros = countZeros + 1

		right = gimmeNumber( 0, maxSummand )
		if right == 0: countZeros = countZeros + 1

	# generate numbers for an subtraction problem
	elif operand == '-':

		left = gimmeNumber( 1, maxMinuend )
		if left == 0: countZeros = countZeros + 1

		right = gimmeNumber( 0, maxSubtrahend if ( left + 1 ) > maxSubtrahend else left + 1 )
		if right == 0: countZeros = countZeros + 1

	# other operations may be supported in the future!
	else:
		print "Sorry, something went wrong."

	# this is the output of one problem to solve
	print( '{} {} {} =' ).format( left, operand, right )

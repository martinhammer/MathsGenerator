import random

# ------------------------------------------
# You can set the following parameters

# how many rows to generate
outputRows = 36 

# mix of operations from which a random selection will be made; proportions can be adjusted, e.g. ++- to get twice as many additions than subtractions
operandMix = '+-*'

# highest number for additions (left hand size)
maxSummandLeft = 20

# highest number for additions (right hand size)
maxSummandRight = 10

# highest number for subtraction left hand side (minuend)
maxMinuend = 20

# highest number for subtraction right hand side (subtrahend)
maxSubtrahend = 10

# highest number for multiplication left hand side (multiplicant)
maxMultiplicant = 10

# highest number for multiplication right hand side (multiplier)
maxMultiplier = 10

# maximum number of zeroes allowed to be generated (too many zeroes make the exercise too easy :))
maxZeros = 2

# ------------------------------------------
# No need to make changes below this line

# current number of zeros
countZeros = 0

def gimmeNumber( minValue, maxValue ):

	global maxZeros
	global countZeros

	randomNumber = random.randrange( minValue, maxValue + 1 )
	while ( randomNumber == 0 ) and ( countZeros >= maxZeros ):
		randomNumber = random.randrange( minValue, maxValue + 1 )

	return randomNumber

# ------------------------------------------

# main loop which generates random problems
for i in range( outputRows ):

	# randomly decide kind of problem to generate
	operand = random.choice( operandMix )

	# generate numbers for an addition problem
	if operand == '+':

		left = gimmeNumber( 0, maxSummandLeft )
		if left == 0: countZeros = countZeros + 1

		right = gimmeNumber( 0, maxSummandRight )
		if right == 0: countZeros = countZeros + 1

	# generate numbers for an subtraction problem
	elif operand == '-':

		left = gimmeNumber( 1, maxMinuend )
		if left == 0: countZeros = countZeros + 1

		right = gimmeNumber( 0, maxSubtrahend if ( left + 1 ) > maxSubtrahend else left + 1 )
		if right == 0: countZeros = countZeros + 1

	elif operand == '*':

		left = gimmeNumber( 0, maxMultiplicant )
		if left == 0: countZeros = countZeros + 1

		right = gimmeNumber( 0, maxMultiplier )
		if right == 0: countZeros = countZeros + 1

	# other operations may be supported in the future!
	else:
		print( 'Sorry, {} operation is not supported.' ).format( operand )
		next

	# this is the output of one problem to solve
	print( '{} {} {} =' ).format( left, operand, right )

import getopt, random, sys, textwrap

# -------------------------------------------------------------------
# sensible defaults for input parameters
outputRows = 10
operandMix = '+-x'
maxZeros = 2
maxSummandLeft = 90
maxSummandRight = 10
maxMinuend = 100
maxSubtrahend = 10
maxMultiplicant = 12
maxMultiplier = 12

# -------------------------------------------------------------------
# keeps track of current number of zeros
countZeros = 0

# -------------------------------------------------------------------
def usage():
	helptext = """    Usage:
    mathsgenerator [-h] [-r outputrows] [-o operands] [-z maxzeros] 
    [-l maxsummandleft] [-r maxsummandright] [-m maxminuend] 
    [-s maxsubtrahend] [-a maxmultiplicant] [-b maxmultiplier] 

    -h, --help: prints this text
    -r, --outputrows: number of equations to be generated
    -o, --operands: mix of operations from which a random selection will be made; proportions can be adjusted, e.g. ++- to get twice as many additions as subtractions
    -z, --maxzeros: maximum number of zeros allowed to be used in equations (too many zeros make the exercise too easy :))
    -l, --maxsummandleft: highest number for additions (left hand size)
    -r, --maxsummandright: highest number for additions (right hand size)
    -m, --maxminuend: highest number for subtraction left hand side (minuend)
    -s, --maxsubtrahend: highest number for subtraction right hand side (subtrahend)
    -a, --maxmultiplicant: highest number for multiplication left hand side (multiplicant)
    -b, --maxmultiplier: highest number for multiplication right hand side (multiplier)
	 """
	print textwrap.dedent( helptext )

# -------------------------------------------------------------------
def main( argv ):

	global outputRows
	global operandMix
	global maxZeros
	global maxSummandLeft
	global maxSummandRight
	global maxMinuend
	global maxSubtrahend
	global maxMultiplicant
	global maxMultiplier
	global countZeros

	try:
		opts, args = getopt.getopt( argv, "hr:o:z:l:r:m:s:a:b:", [ "help", "outputrows=", "operands=", "maxzeros=", "maxsummandleft=", "maxsummandright=", "maxminuend=", "maxsubtrahend=", "maxmultiplicant=", "maxmultiplier=" ] )
	except getopt.GetoptError:
		usage()                         
		sys.exit( 2 )                   
	for opt, arg in opts:
		if opt in ( "-h", "--help" ):
			usage()
			sys.exit()
		elif opt in ( "-r", "--outputrows" ):
			outputRows = int( arg )
		elif opt in ( "-o", "--operands" ):
			operandMix = arg
		elif opt in ( "-z", "--maxzeros" ):
			maxZeros = int( arg )
		elif opt in ( "-l", "--maxsummandleft" ):
			maxSummandLeft = int( arg )
		elif opt in ( "-r", "--maxsummandright" ):
			maxSummandRight = int( arg )
		elif opt in ( "-m", "--maxminuend" ):
			maxMinuend = int( arg )
		elif opt in ( "-s", "--maxsubtrahend" ):
			maxSubtrahend = int( arg )
		elif opt in ( "-a", "--maxmultiplicant" ):
			maxMultiplicant = int( arg )
		elif opt in ( "-b", "--maxmultiplier" ):
			maxMultiplier = int( arg )

	for i in range( outputRows ):
		# randomly decide kind of problem to generate
		operand = random.choice( operandMix )
		# addition problem
		if operand == '+':
			left = gimmeNumber( 0, maxSummandLeft )
			if left == 0: countZeros = countZeros + 1
			right = gimmeNumber( 0, maxSummandRight )
			if right == 0: countZeros = countZeros + 1
			printEquation( left, operand, right )
		# subtraction problem
		elif operand == '-':
			left = gimmeNumber( 1, maxMinuend )
			if left == 0: countZeros = countZeros + 1
			right = gimmeNumber( 0, maxSubtrahend if ( left ) > maxSubtrahend else left )
			if right == 0: countZeros = countZeros + 1
			printEquation( left, operand, right )
		# multiplication problem
		elif operand == 'x':
			left = gimmeNumber( 0, maxMultiplicant )
			if left == 0: countZeros = countZeros + 1
			right = gimmeNumber( 0, maxMultiplier )
			if right == 0: countZeros = countZeros + 1
			printEquation( left, operand, right )
		# other operations may be supported in the future!
		else:
			print( 'Sorry, {} operation is not supported.' ).format( operand )
			next

# -------------------------------------------------------------------
def gimmeNumber( minValue, maxValue ):

	global maxZeros
	global countZeros

	randomNumber = random.randrange( minValue, maxValue + 1 )
	while ( randomNumber == 0 ) and ( countZeros >= maxZeros ):
		randomNumber = random.randrange( minValue, maxValue + 1 )

	return randomNumber

# -------------------------------------------------------------------
def printEquation( left, operand, right ):
	print( '{} {} {} =' ).format( left, operand, right )

# -------------------------------------------------------------------
if __name__ == "__main__":
	main( sys.argv[1:] )

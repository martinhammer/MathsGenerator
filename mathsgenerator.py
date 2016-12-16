import getopt, random, sys, textwrap

# -------------------------------------------------------------------
# sensible defaults for input parameters
outputRows = 10
operandMix = '+-x/'
maxZeros = 2
maxSummandLeft = 90
maxSummandRight = 10
maxMinuend = 100
maxSubtrahend = 10
maxMultiplicant = 12
maxMultiplier = 12
maxFactor = 12
maxDivisor = 12

# -------------------------------------------------------------------
# keeps track of current number of zeros
countZeros = 0

# are we using a maximum value or a specific list for multiplication and division
useListForMultiply = False
useListForDivide = False

# -------------------------------------------------------------------
# some global constants
PARAM_INT = 1
PARAM_LIST = 2

# -------------------------------------------------------------------
def usage():
	helptext = """    Usage:
    mathsgenerator [-h] [-g outputrows] [-o operands] [-z maxzeros] 
    [-l maxsummandleft] [-r maxsummandright] [-m maxminuend] 
    [-s maxsubtrahend] [-a maxmultiplicant] [-b maxmultiplier] 
    [-v multipliervalues] [-f maxfactor] [-d maxdivisor] 
    [-w divisorvalues]

    -h, --help: prints this text
    -f, --configfile: configuration file from which settings are read
    -e, --configsection: section within the configuration file from which settings are read
    -g, --outputrows: number of equations to be generated
    -o, --operands: mix of operations from which a random selection will be made; proportions can be adjusted, e.g. ++- to get twice as many additions as subtractions
    -z, --maxzeros: maximum number of zeros allowed to be used in equations (too many zeros make the exercise too easy :))
    -l, --maxsummandleft: highest number for additions (left hand size)
    -r, --maxsummandright: highest number for additions (right hand size)
    -m, --maxminuend: highest number for subtraction left hand side (minuend)
    -s, --maxsubtrahend: highest number for subtraction right hand side (subtrahend)
    -a, --maxmultiplicant: highest number for multiplication left hand side (multiplicant)
    -b, --maxmultiplier: highest number for multiplication right hand side (multiplier)
    -v, --multipliervalues: comma separated list of values for multiplication right hand side (multiplier); if this option is specified, then -b / --maxmultiplier is ignored
    -f, --maxfactor: highest number for factor in division (maximum left hand side - dividend - is calculated by using the factor and divisor)
    -d, --maxdivisor: highest number for division right hand size (divisor)
    -w, --divisorvalues: comma separated list of values for division right hand side (divisor); if this option is specified, then -d / --maxdivisor is ignored
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
	global multiplierValues
	global maxFactor
	global maxDivisor
	global divisorValues
	global countZeros
	global useListForMultiply
	global useListForDivide
	global PARAM_INT
	global PARAM_LIST

	try:
		opts, args = getopt.getopt( argv, "hg:o:z:l:r:m:s:a:b:v:f:d:w:", [ "help", "outputrows=", "operands=", "maxzeros=", "maxsummandleft=", "maxsummandright=", "maxminuend=", "maxsubtrahend=", "maxmultiplicant=", "maxmultiplier=", "multipliervalues=", "maxfactor=", "maxdivisor=", "divisorvalues=" ] )
	except getopt.GetoptError:
		usage()
		sys.exit( 2 )
	for opt, arg in opts:
		if opt in ( "-h", "--help" ):
			usage()
			sys.exit()
		elif opt in ( "-g", "--outputrows" ):
			outputRows = validateInput( opt, arg, PARAM_INT )
		elif opt in ( "-o", "--operands" ):
			operandMix = arg
		elif opt in ( "-z", "--maxzeros" ):
			maxZeros = validateInput( opt, arg, PARAM_INT )
		elif opt in ( "-l", "--maxsummandleft" ):
			maxSummandLeft = validateInput( opt, arg, PARAM_INT )
		elif opt in ( "-r", "--maxsummandright" ):
			maxSummandRight = validateInput( opt, arg, PARAM_INT )
		elif opt in ( "-m", "--maxminuend" ):
			maxMinuend = validateInput( opt, arg, PARAM_INT )
		elif opt in ( "-s", "--maxsubtrahend" ):
			maxSubtrahend = validateInput( opt, arg, PARAM_INT )
		elif opt in ( "-a", "--maxmultiplicant" ):
			maxMultiplicant = validateInput( opt, arg, PARAM_INT )
		elif opt in ( "-b", "--maxmultiplier" ):
			maxMultiplier = validateInput( opt, arg, PARAM_INT )
		elif opt in ( "-v", "--multipliervalues" ):
			useListForMultiply = True
			multiplierValues = validateInput( opt, arg, PARAM_LIST )
		elif opt in ( "-f", "--maxfactor" ):
			maxFactor = validateInput( opt, arg, PARAM_INT )
		elif opt in ( "-d", "--maxdivisor" ):
			maxDivisor = validateInput( opt, arg, PARAM_INT )
		elif opt in ( "-w", "--divisorvalues" ):
			useListForDivide = True
			divisorValues = validateInput( opt, arg, PARAM_LIST )

	for i in range( outputRows ):
		# randomly decide kind of problem to generate
		operand = random.choice( operandMix )
		# addition problem
		if operand == '+':
			left = gimmeRandomNumber( 0, maxSummandLeft )
			right = gimmeRandomNumber( 0, maxSummandRight )
			printEquation( left, operand, right )
		# subtraction problem
		elif operand == '-':
			left = gimmeRandomNumber( 1, maxMinuend )
			right = gimmeRandomNumber( 0, maxSubtrahend if ( left ) > maxSubtrahend else left )
			printEquation( left, operand, right )
		# multiplication problem
		elif operand == 'x':
			left = gimmeRandomNumber( 0, maxMultiplicant )
			if useListForMultiply:
				right = gimmeListNumber( multiplierValues )
			else:
				right = gimmeRandomNumber( 0, maxMultiplier )
			printEquation( left, operand, right )
		# division problem
		elif operand == '/':
			if useListForDivide:
				right = gimmeListNumber( divisorValues )
			else:
				right = gimmeRandomNumber( 1, maxDivisor )
			left = gimmeRandomNumber( 1, maxFactor ) * right
			printEquation( left, operand, right )
		# other operations may be supported in the future!
		else:
			print 'Sorry, operation "' + operand + '" is not supported.'
			next

# -------------------------------------------------------------------
def validateInput( opt, arg, argtype ):

	global PARAM_INT
	global PARAM_LIST

	if argtype == PARAM_INT:
		try:
			val = int( arg )
		except ValueError:
			print 'Please supply a positive integer value for parameter "' + opt + '".'
			sys.exit( 3 )
		if val <= 0:
			print 'Please supply a positive integer value for parameter "' + opt + '".'
			sys.exit( 3 )
		return val

	elif argtype == PARAM_LIST:
		values = []
		try: 
			for item in arg.split( ","):
				try:
					val = int( item )
					if val < 0:
						print 'Please supply only non-negative integer values for parameter "' + opt + '".'
						sys.exit( 3 )
					values.append( val )
				except ValueError:
					print 'Please supply non-negative integer values for parameter "' + opt + '".'
					sys.exit( 3 )
		except AttributeError:
			print 'Please supply a list of integer values for parameter "' + opt + '".'
			sys.exit( 3 )
		return values

# -------------------------------------------------------------------
def gimmeRandomNumber( minValue, maxValue ):

	global maxZeros
	global countZeros

	randomNumber = random.randrange( minValue, maxValue + 1 )
	while ( randomNumber == 0 ) and ( countZeros >= maxZeros ):
		randomNumber = random.randrange( minValue, maxValue + 1 )

	if randomNumber == 0: countZeros = countZeros + 1
	return randomNumber

# -------------------------------------------------------------------
def gimmeListNumber( possibleValues ):

	global maxZeros
	global countZeros

	randomNumber = random.choice( possibleValues )
	# ignore maxZeroes parameter if the list of values only has zero in it, in order to prevent an infinite loop
	if not( len( possibleValues ) == 1 and ( possibleValues[0] == 0 ) ):
		while ( randomNumber == 0 ) and ( countZeros >= maxZeros ):
			randomNumber = random.choice( possibleValues )

	if randomNumber == 0: countZeros = countZeros + 1
	return randomNumber

# -------------------------------------------------------------------
def printEquation( left, operand, right ):
	print( '{} {} {} =' ).format( left, operand, right )

# -------------------------------------------------------------------
if __name__ == "__main__":
	main( sys.argv[1:] )

Maths Generator
===============
 
This is a script to generate simple maths problems which can be printed out and solved as homework.  

Example 0: print help text.
```
$ python mathsgenerator.py -h
Usage:
mathsgenerator [-h] [-p separator] [-g outputrows] [-o operands] [-z maxzeros]
[-l maxsummandleft] [-r maxsummandright] [-m maxminuend] [-s maxsubtrahend]
[-a maxmultiplicant] [-b maxmultiplier] [-v multipliervalues] [-f maxfactor] 
[-d maxdivisor] [-w divisorvalues]

All parameters are optional, "sensible" default values will be used for any configurable setting if the option is not provided.

-h, --help: prints this text
-p, --separator: delimiter for the output (default is space)
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
```

Example 1: simple addition and subtraction problems.
```
$ python mathsgenerator.py --outputrows=30 --operands=+- --maxzeros=2 --maxsummandleft=20 --maxsummandright=10 --maxminuend=20 --maxsubtrahend=10
```

Example 2: more advanced problems, including multiplication and division with selected value.
```
$ python mathsgenerator.py --outputrows=30 --operands=+-x/ --maxzeros=2 --maxsummandleft=90 --maxsummandright=10 --maxminuend=100 --maxsubtrahend=10 --maxmultiplicant=12 --multipliervalues=2,3,4,5 --maxfactor=10 --divisorvalues=2,3,4,5
```

'''
Author: Matthew Mettler
Project Euler, Problem 27
https://projecteuler.net/problem=27

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.

Status: Complete?
-59231
[Finished in 3.6s]
'''
import math
import operator

values = range(-999,1001)
primeTable = {}
maxCoefficients = 0, 0
maxChain = 0

def product(iterable):
	return reduce(operator.mul, iterable, 1)

def isPrime(n):
	if n <= 0: return False
	if n in primeTable: pass
	else: primeTable[n] = not [x for x in range(2, int(math.sqrt(n))+1) if n%x == 0]
	return primeTable[n]

def solveQuadratic(n, a, b):
	return n*n + a*n + b

def consecutivePrimes(a, b):
	length = 0
	while True:
		if not isPrime(solveQuadratic(length, a, b)):
			break
		length += 1
	return length

for a in values:
	for b in values:
		if (consecutivePrimes(a,b) > maxChain):
			maxCoefficients = a, b
			maxChain = consecutivePrimes(a,b)

print(product(maxCoefficients))
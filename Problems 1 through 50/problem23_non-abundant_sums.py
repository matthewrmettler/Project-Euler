'''
Author: Matthew Mettler
Project Euler, Problem 23
https://projecteuler.net/problem=23

A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors
of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect
number.

A number whose proper divisors are less than the number is called
deficient and a number whose proper divisors exceed the number is called
abundant.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the
smallest number that can be written as the sum of two abundant numbers is
24. By mathematical analysis, it can be shown that all integers greater
than 28123 can be written as the sum of two abundant numbers. However,
this upper limit cannot be reduced any further by analysis even though it
is known that the greatest number that cannot be expressed as the sum of
two abundant numbers is less than this limit.

#Every integer greater than 20161 can be written as the sum of two abundant numbers.
#According to wiki

Find the sum of all the positive integers which cannot be written as the
sum of two abundant numbers.

Status: Correct
'''
import math
import itertools
from collections import Counter

primeNumbers = []
primeFactors = {}
abundantNumbers = []
nonSum = [] #numbers to add together for final answer
upperLimit = 28123
#upperLimit = 100

def isPrime(n):
	if n <= 0: return False
	return not [x for x in xrange(2, int(math.sqrt(n))+1) if n%x == 0]

def generatePrimes(upperLimit):
	for n in range(2, upperLimit+1):
		if not [x for x in xrange(2, int(math.sqrt(n))+1) if n%x == 0]:
			primeNumbers.append(n)

def getPrimeFactors(n):
	if n < 0 or n > upperLimit:
		return []
	if n in primeFactors:
		return primeFactors[n]
	primes = []
	if n in primeNumbers:
		primes.append(n)
	#else, not prime
	else:
		for x in primeNumbers:
			if x > n: break
			if n % x == 0:
				primes.append(x)
				list = getPrimeFactors(n/x)
				for i in list:
					primes.append(i)
				break
	return primes

def sumOfProperDivisors(n):
	dict = Counter(getPrimeFactors(n))
	keyproduct = 1
	for k, v in dict.items():
		keysum = 0
		for i in range(0,v+1):
			keysum += k**i
		keyproduct *= keysum
	result = keyproduct - n 
	return result

def isAbundant(n):
	if n in primeNumbers:
		return False #all prime numbers are deficient
	return sumOfProperDivisors(n) > n

def getNonSum():
	count = 0
	nonSum = range(upperLimit)
	#print(len(nonSum))
	for x in abundantNumbers:
		for y in abundantNumbers:
			if x + y >= upperLimit:
				break
			nonSum[x+y] = 0
	print("Sum is " + str(sum(nonSum)))


#generate abundant number
def generateAbundantNumbers(upperLimit):
	for i in range(12,upperLimit):
		if isAbundant(i):
			abundantNumbers.append(i)

def main():
	generatePrimes(upperLimit)
	generateAbundantNumbers(upperLimit)
	print("Generated %s abundantNumbers" % len(abundantNumbers))
	getNonSum()

if __name__ == "__main__":
	main()
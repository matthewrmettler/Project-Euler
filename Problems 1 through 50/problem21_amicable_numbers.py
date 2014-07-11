'''
Author: Matthew Mettler
Project Euler, Problem 21
https://projecteuler.net/problem=21

Let d(n) be defined as the sum of proper divisors of n (numbers less than
   n which divide evenly into n).
   If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and
   each of a and b are called amicable numbers.

   For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22,
   44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1,
   2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

Status: Complete, not sure if correct
Site is down, so I can't check, but it returned:
5736396

after 1.1 seconds
'''
import math
from collections import Counter

primeNumbers = []
primeFactors = {}
amicableNumbers = []
upperLimit = 10000

def isPrime(n):
	if n <= 0: return False
	return not [x for x in xrange(2, int(math.sqrt(n))+1) if n%x == 0]

def generatePrimes(upperLimit):
	primeNumbers.append(2)
	primeNumbers.append(3)
	for n in range(2, upperLimit+1):
		if not [x for x in xrange(2, int(math.sqrt(n))+1) if n%x == 0]:
			primeNumbers.append(n)

def getPrimeFactors(n):
	if n < 0 or n > 10000:
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
			keysum += k**v
		keyproduct *= keysum
	result = keyproduct - n 
	return result

def checkAmicable(n):
	if (n%100 == 0): print("checkAmicable: " + str(n))
	sum = sumOfProperDivisors(n)
	if n == sumOfProperDivisors(sum):
		amicableNumbers.append(n)

#main
generatePrimes(upperLimit)
for i in range(2,10001):
	#getPrimeFactors(i)
	checkAmicable(i)

print(sum(amicableNumbers))

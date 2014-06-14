'''
Author: Matthew Mettler
Project Euler, Problem 10
https://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

Status: Correct, but slow (~10 seconds?)
'''
import math

primes = [2]

count = 3
def addPrime(num):
	global primes
	end = int(math.ceil(math.sqrt(num)))
	for i in range(2, end+1):
		if num % i == 0:
			return False
	#is prime
	primes.append(num)
	return True

while primes[-1] < 2000000:
	addPrime(count)
	count += 1

if primes[-1] >= 2000000:
	del primes[-1]

print(sum(primes))

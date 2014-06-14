'''
Author: Matthew Mettler
Project Euler, Problem 7
https://projecteuler.net/problem=7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

Status: Correct
'''
import math

prime = [2]

count = 3
def addPrime(num):
	end = int(math.ceil(math.sqrt(num)))
	for i in range(2, end+1):
		if num % i == 0:
			return False
	#is prime
	prime.append(num)
	return True

while len(prime) < 10001:
	addPrime(count)
	count += 1

print(str(prime[-1]))
"""
Author: Matthew Mettler
Project Euler, Problem 47
https://projecteuler.net/problem=47
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 x 7
15 = 3 x 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2^2 x 7 x 23
645 = 3 x 5 x 43
646 = 2 x 17 x 19

Find the first four consecutive integers to have four distinct prime factors. 
What is the first of these numbers?

Status: Incomplete
"""
from math import sqrt

primes = []

def isPrime(n):
	if n < 2: return False
	if n == 2: return True
	if n % 2 == 0: return False
	for i in range(3,int(sqrt(n))+1):
		if n % i == 0: return False
	return True

def generate_primes(n):
	for i in range(n):
		if isPrime(i):
			primes.append(i)

def generate_prime_factors(n):
	temp = n
	prime_factors = []
	for prime in primes:
		while(temp % prime == 0):
			temp = temp/prime
			prime_factors.append(prime)
		if (temp == 1): break
	return(prime_factors)

def check_consecutive_integers(n):
	factors = []
	for i in range(n, n+4):
		pf = generate_prime_factors(i)
		if len(set(pf)) != 4:
			return False
		factors.append(pf)

	#Guaranteed length 4: check for uniqueness
	if ((factors[0] == factors[1]) or (factors[0] == factors[2]) or 
		(factors[0] == factors[3]) or (factors[1] == factors[2]) or 
		(factors[1] == factors[3]) or (factors[2] == factors[3])):
			return False
	return True


def main():
	generate_primes(100000)
	for i in range(2,150000):
		if (check_consecutive_integers(i)):
			print(i)

if __name__ == "__main__":
	main()
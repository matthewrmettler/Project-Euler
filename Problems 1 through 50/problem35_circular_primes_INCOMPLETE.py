'''
Author: Matthew Mettler
Project Euler, Problem 35
https://projecteuler.net/problem=35

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

Status: Incomplete
'''
from math import sqrt
primes = [2]

def isPrime(num):
	global primes
	if num % 2 == 0: return False
	for i in [x for x in primes if primes <= sqrt(num)]:
		if num % i == 0: return False
	primes.append(num)
	return True

#get first million primes
for n in range(3, 1000000): isPrime(n)

print(len(primes))
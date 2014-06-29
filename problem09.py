'''
Author: Matthew Mettler
Project Euler, Problem 9
https://projecteuler.net/problem=9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Status: Correct
'''
from math import sqrt

def isTriplet(a, b, c):
	return (a**2 + b**2 == c**2)

def sumToThousand(a, b, c):
	return (a + b + c == 1000)

for i in range(1, 1001):
	for j in range(1000-i, i, -1):
			k = int(sqrt(i**2 + j**2))
			if sumToThousand(i, j, k) and isTriplet(i, j, k):
				print(str(i*j*k))
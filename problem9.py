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
import math

def isTriplet(a, b, c):
	return (math.pow(a,2) + math.pow(b,2) == math.pow(c, 2))

def sumToThousand(a, b, c):
	return (a + b + c == 1000)

for i in range(1, 1000):
	for j in range(1000-i, i, -1):
			k = int(math.sqrt(math.pow(i, 2) + math.pow(j, 2)))
			if sumToThousand(i, j, k) and isTriplet(i, j, k):
				print(str(i*j*k))
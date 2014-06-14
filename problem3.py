'''
Author: Matthew Mettler
Project Euler, Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

Status: Correct
'''
import math

baseNumber = 600851475143
primeFactors = []
number = baseNumber

for i in range(2, int(math.floor(math.sqrt(baseNumber)))):
	if number % i == 0:
		primeFactors.append(i)
		number = number / i
		i = 2

print(primeFactors[-1])

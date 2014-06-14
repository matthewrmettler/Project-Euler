'''
Author: Matthew Mettler
Project Euler, Problem 6
https://projecteuler.net/problem=6

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

Status: Correct
'''
import math

#Try naive approach to see runtime -- runtime is fine

def sumOfSquares(number):
	sum = 0
	for i in range(1, number+1):
		sum = sum + math.pow(i, 2)
	return sum

def squareOfSums(number):
	sum = 0
	for i in range(1, number+1):
		sum = sum + i
	return math.pow(sum, 2)

print(str(sumOfSquares(100) - squareOfSums(100)))

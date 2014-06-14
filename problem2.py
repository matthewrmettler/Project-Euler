'''
Author: Matthew Mettler
Project Euler, Problem 2

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

Status: Correct
'''
import math

sum = 0

fibonacci = [1,2]

def nextFib():
	fibonacci.append(fibonacci[-1] + fibonacci[-2])

	return fibonacci[-1]

while fibonacci[-1] < 4000000:
	nextFib()

fibonacci = fibonacci[0:-1]

sum = 0
for num in fibonacci:
	if num%2 == 0:
		sum = sum + num
print sum



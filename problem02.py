'''
Author: Matthew Mettler
Project Euler, Problem 2

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

Status: Correct
'''
fibonacci = [1,2]

def nextFib():
	fibonacci.append(fibonacci[-1] + fibonacci[-2])

while fibonacci[-1] < 4000000: 
	nextFib()

fibonacci = fibonacci[0:-1]

print(sum(x for x in fibonacci if x % 2 == 0))
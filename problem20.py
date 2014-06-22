'''
Author: Matthew Mettler
Project Euler, Problem 20
https://projecteuler.net/problem=20

Find the sum of the digits in the number 100!

Status: Correct. Had trouble iterating over the generator object created by math.factorial, so I just defined it here.
Saving the values in an array isn't necessary for such a small n, but I figured I might as well
'''
NUMBER = 100000000
facts = [1]
def factorial(n):
	if n <= len(facts): 
		return facts[n-1]
	else: 
		facts.append(n * factorial(n-1))
		return facts[-1]

def genFacts(n):
	for i in range(1,n+1):
		factorial(i)

def sumDigits(n):
	return sum([int(x) for x in str(factorial(n))])

#main code
genFacts(NUMBER)
print (sumDigits(NUMBER))

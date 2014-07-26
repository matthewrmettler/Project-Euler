'''
Author: Matthew Mettler
Project Euler, Problem 20
https://projecteuler.net/problem=20

Find the sum of the digits in the number 100!

Status: Correct. 
'''
number = 100
facts = [1]
def factorial(n):
	if n <= len(facts): return facts[n-1]
	else: 
		facts.append(n * factorial(n-1))
		return facts[-1]

def generate_factorials():
	for i in range(number+1):
		factorial(i)

#main code
generate_factorials()
print (sum([int(x) for x in str(factorial(number))]))

'''
Author: Matthew Mettler
Project Euler, Problem 41
https://projecteuler.net/problem=41

We shall say that an n-digit number is pandigital if it makes use of all the 
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and 
is also prime.

What is the largest n-digit pandigital prime that exists?
Status: Correct
'''
from math import sqrt
import itertools

def is_prime(num):
	if num <= 1: return False
	if num == 2: return True
	if num % 2 == 0: return False
	for i in range(3, int(sqrt(num))+2,2):
		if num % i == 0: return False
	return True

def main():
	maxVal = 0
	for n in range(2,9):
		digits = [str(x) for x in range(1,n+1)]
		permutes = itertools.permutations(digits)
		for item in permutes:
			item = int(''.join(item))
			if (is_prime(item)):
				maxVal = max(maxVal, item)
	print(maxVal)

if __name__ == "__main__":
	main()
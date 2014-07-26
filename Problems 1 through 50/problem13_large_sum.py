'''
Author: Matthew Mettler
Project Euler, Problem 13
https://projecteuler.net/problem=13

Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

Status: Correct
'''
filename = 'problem13_data.txt'

numbers = []
with open(filename) as f:
	for line in f:
		numbers.append(''.join(line[:-1]))

print(str(sum([int(x[:11]) for x in numbers]))[:10])


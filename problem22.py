'''
Author: Matthew Mettler
Project Euler, Problem 22
https://projecteuler.net/problem=22

What is the total of all the name scores in the file?

Status: Complete, not submitted officially
871198282
Correct according to https://code.google.com/p/projecteuler-solutions/wiki/ProjectEulerSolutions
[Finished in 0.1s]
'''
import math

filename = 'problem22_data.txt'

value_offset = 64
def value(name, count):
	sum = 0
	for letter in name:
		sum += ord(letter) - value_offset
	return sum*count

with open(filename) as f:
	names = sorted(f.read().replace('"', '').split(','))
	count = 1
	total = 0
	for n in names:
		total += value(n, count)
		count += 1
	print(total)
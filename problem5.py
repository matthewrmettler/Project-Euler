'''
Author: Matthew Mettler
Project Euler, Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Status: Correct
'''
import math

number = 20

def divisible(number):
	for i in range(1, 20):
		if number % i != 0:
			return False
	return True

while(not divisible(number)):
	number += 20

print(number)
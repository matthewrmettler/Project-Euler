'''
Author: Matthew Mettler
Project Euler, Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the 
numbers from 1 to 20?

Status: Correct
'''
low = 1
high = 20

# Don't need to check lower terms since being divided by 20 implies 
# divisibility by 1, 2, etc.
def getRange(low, high):
	values = range(low, high+1)
	for i in range(high, low-1, -1):
		for j in range(low, i):
			if i % j == 0:
				if j in values: values.remove(j)
	return values

divide_range = getRange(low, high)
def divisible(low, high, number):
	for i in divide_range:
		if number % i != 0:
			return False
	return True

def smallestPossible(low, high):
	num = high
	while(not divisible(low, high, num)): num += high
	print(num)

smallestPossible(low, high)
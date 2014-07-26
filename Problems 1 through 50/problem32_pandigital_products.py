'''
Author: Matthew Mettler
Project Euler, Problem 32
https://projecteuler.net/problem=32

Find the sum of all products whose multiplicand/multiplier/product identity 
can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only 
include it once in your sum.

Status: Correct
I couldn't think of an elegant to figure out the 'a * b = c, make sure the sum 
of digits is 9, and filter those that are impossible.'
'''
from itertools import permutations
from time import sleep
def multichoose(n,k):
    if k < 0 or n < 0: return "Error"
    if not k: return [[0]*n]
    if not n: return []
    if n == 1: return [[k]]
    return [[0]+val for val in multichoose(n-1,k)] + \
        [[val[0]+1]+val[1:] for val in multichoose(n,k-1)]

pandigits = list(map("".join, permutations("123456789")))
valid_products = []

splits = [x for x in multichoose(3,9) if 0 not in x if x[2] is not 1]

#curate splits just based on impossible splits (ie a 1 digit number times a 1 digit number cannot be a 7 digit number)
splits.remove([1, 1, 7])
splits.remove([1, 2, 6])
splits.remove([1, 3, 5])
splits.remove([1, 5, 3])
splits.remove([1, 6, 2])
splits.remove([2, 1, 6])
splits.remove([2, 4, 3])
splits.remove([2, 5, 2])
splits.remove([3, 1, 5])
splits.remove([3, 3, 3])
splits.remove([3, 4, 2])
splits.remove([4, 2, 3])
splits.remove([4, 3, 2])
splits.remove([5, 1, 3])
splits.remove([5, 2, 2])
splits.remove([6, 1, 2])
print(len(splits))
print(splits)
for split in splits:
	#print(split)
	for item in pandigits:
		x = item[:split[0]]
		y = item[split[0]:split[0]+split[1]]
		z = item[-split[2]:]
		if int(x) * int(y) == int(z): 
			print("{} x {} = {} ".format(x, y, z))
			valid_products.append(int(z))
		#sleep(1)
print(len(valid_products))
print(sum(set(valid_products)))




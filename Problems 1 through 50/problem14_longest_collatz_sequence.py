'''
Author: Matthew Mettler
Project Euler, Problem 14
https://projecteuler.net/problem=14

Which starting number, under one million, produces the longest Collatz Problem 
chain?

Status: Complete, 3.1 seconds on laptop
I like the use of a dictionary to store the values; debated using a graph or a 
list, but a list would have an unknown max size,and a tree would have very 
little branches to make it worthwhile compared to a dictioary.
'''
import operator

#use dictionary to store intermediate values, get length recursively
lengths = {}
def getLength(num):
	if num == 1: return 1
	if num in lengths: return lengths[num]
	if num % 2 == 0: return 1+getLength(num/2)
	return 1+getLength(3*num + 1)

for i in range(2,1000000):
	lengths[i] = getLength(i)

print(max(lengths.iteritems(), key=operator.itemgetter(1))[0])


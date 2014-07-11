'''
Author: Matthew Mettler
Project Euler, Problem 18
https://projecteuler.net/problem=18

Find the maximum total from top to bottom of the triangle.

Status: Complete
Happy with this solution
'''
import math

filename = 'problem18_data.txt'

triangle = []
with open(filename) as f:
	for line in f:
		triangle.append(map(int, line[:-1].split(' ')))
print(triangle)
#read from second-to-last row the two possible paths, choose the maximum of the sums, replace value. Repeat all the way up
for layer in range(len(triangle)-2, -1, -1):
	for item in range(0, len(triangle[layer])):
		triangle[layer][item] += max(triangle[layer+1][item], triangle[layer+1][item+1])

print(triangle[0][0])
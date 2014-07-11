'''
Author: Matthew Mettler
Project Euler, Problem 11
https://projecteuler.net/problem=11

What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?

Status: Complete
'''
import math
grid = []
filename = 'problem11_data.txt'
maxProduct = 0

#read number from file
with open(filename) as f:
	for i in range(0,20):
		grid.append(f.readline()[:-1].split(' '))

for i in range(0, 16):
	for j in range(0, 16):
		#row
		row = 1
		col = 1
		diag_down = 1
		diag_up = 1
		for num in range(0, 4):
			row *= int(grid[i][j+num])
			col *= int(grid[i+num][j])
			diag_down *= int(grid[i+num][j+num])
			diag_up *= int(grid[i+num][+3+j-num])
		maxProduct = max(maxProduct, row, col, diag_down, diag_up)

print(maxProduct)
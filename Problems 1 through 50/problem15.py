'''
Author: Matthew Mettler
Project Euler, Problem 15
https://projecteuler.net/problem=15

Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?

Status: Complete
Happy with this solution
'''

#recursively build a grid of the VERTICES
grid = []
for i in range(0,21):
	grid.append([0]*21)

#set last row and last column to 1s
for i in range(0,21):
	grid[20][i] = 1
	grid[i][20] = 1

#number of paths for x,y is equal to sum of paths below and to the right
def calc(x, y):
	grid[x][y] = grid[x+1][y] + grid[x][y+1]

#calculate
for i in range(19, -1, -1):
	for j in range(19, -1, -1):
		calc(i,j)

#solution
print(grid[0][0])
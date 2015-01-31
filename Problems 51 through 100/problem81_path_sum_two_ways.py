'''
Author: Matthew Mettler
Project Euler, Problem 81
https://projecteuler.net/problem=81

Find the minimal path sum, in matrix.txt, a 31K text file containing a 80 by 80
 matrix, from the top left to the bottom right by only moving right and down.

Status: Incomplete
'''

matrix = []
sum_matrix = []
#file = 'problem81_matrix.txt'
file = 'test_matrix.txt'
with open(file, 'r') as f:
	for line in f:
		matrix.append(map(int, line.split(',')))

size = len(matrix[0])
sum_matrix = [x[:] for x in [[999*(size*2)]*size]*size]

#initialize bottom and right side
sum_matrix[size-1][size-1] = matrix[size-1][size-1]
for i in range(size-2, -1, -1):
	sum_matrix[size-1][i] = matrix[size-1][i] + sum_matrix[size-1][i+1]
	sum_matrix[i][size-1] = matrix[i][size-1] + sum_matrix[i+1][size-1]
	
#dynamic programming approach
for x in range(size-2, -1, -1):
	for y in range(size-2, -1, -1):
		sum_matrix[x][y] = min(sum_matrix[x][y], matrix[x][y] + sum_matrix[x+1][y], matrix[x][y] + sum_matrix[x][y+1])
		for line in sum_matrix:
			print(line)
		print("---")

print(sum_matrix[0][0])

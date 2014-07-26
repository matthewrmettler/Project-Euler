'''
Author: Matthew Mettler
Project Euler, Problem 24
https://projecteuler.net/problem=24

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

Status: Correct
'''
from itertools import permutations

print(''.join(map(str, list(permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))[999999])))


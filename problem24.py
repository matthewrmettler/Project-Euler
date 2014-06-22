'''
Author: Matthew Mettler
Project Euler, Problem 24
https://projecteuler.net/problem=24

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

Status: Complete
Correct according to https://code.google.com/p/projecteuler-solutions/wiki/ProjectEulerSolutions
(2, 7, 8, 3, 9, 1, 5, 6, 0, 4)
[Finished in 1.5s]
'''
from itertools import permutations

print(list(permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))[999999])


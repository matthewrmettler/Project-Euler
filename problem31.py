'''
Author: Matthew Mettler
Project Euler, Problem 31
https://projecteuler.net/problem=31

How many different ways can £2 be made using any number of coins?

Status: Incomplete, trying to do in one line
Correct according to https://code.google.com/p/projecteuler-solutions/wiki/ProjectEulerSolutions
[Finished in 3.6s]
'''
print(len(set([x for x in ([x] for x in range(0,201))])))
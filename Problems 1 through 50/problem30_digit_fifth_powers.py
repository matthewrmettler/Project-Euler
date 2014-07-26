'''
Author: Matthew Mettler
Project Euler, Problem 30
https://projecteuler.net/problem=30

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

Status: Correct
'''
print(sum([x for x in range(2,1000000) if sum(int(y)**5 for y in str(x)) == x]))
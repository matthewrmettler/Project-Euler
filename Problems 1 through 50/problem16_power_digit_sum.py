'''
Author: Matthew Mettler
Project Euler, Problem 16
https://projecteuler.net/problem=16

What is the sum of the digits of the number 2^1000?

Status: Complete
'''
print(sum([int(x) for x in str(2**1000)]))
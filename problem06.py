'''
Author: Matthew Mettler
Project Euler, Problem 6
https://projecteuler.net/problem=6

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

Status: Correct
'''
#Try naive approach to see runtime -- runtime is fine
print( sum((x**2 for x in range(101))) - sum(range(101))**2 ) 

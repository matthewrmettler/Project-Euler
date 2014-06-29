'''
Author: Matthew Mettler
Project Euler, Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.

Status: Correct
'''
print(max([x*y for x in range(999) for y in range(999) if str(x*y) == str(x*y)[::-1]]))


'''
Author: Matthew Mettler
Project Euler, Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.

Status: Correct
'''
import math

largest = 0

def isPalindrome(num):
	return str(num) == str(num)[::-1]

for i in range(1, 999):
	for j in range(1, 999):
		if largest < i*j and isPalindrome(i*j):
			largest = i*j

print(largest)


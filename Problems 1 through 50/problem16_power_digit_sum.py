'''
Author: Matthew Mettler
Project Euler, Problem 16
https://projecteuler.net/problem=16

What is the sum of the digits of the number 2^1000?

Status: Complete
'''
def sumDigits(num):
	sum = 0
	for n in str(num):
		sum += int(n)
	print(sum)

sumDigits(2**1000)



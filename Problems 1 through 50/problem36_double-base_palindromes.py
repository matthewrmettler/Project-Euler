'''
Author: Matthew Mettler
Project Euler, Problem 36
https://projecteuler.net/problem=36

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in 
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include 
leading zeros.)

Status: Correct
'''

def toBinary(decimal):
	return bin(decimal)[2:]

def doublePalindrome(number):
	return (str(number) == str(number)[::-1] and toBinary(number) == toBinary(number)[::-1])

print(sum([int(x) for x in range(1000000) if doublePalindrome(x)]))
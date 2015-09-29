'''
Author: Matthew Mettler
Project Euler, Problem 40
https://projecteuler.net/problem=40

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000
Status: Correct
'''
digits = ""
#500,000 is arbitrary; I just needed the string to contain at least 1 million digits
for i in range(500000):
    digits += str(i)

#Since I started the range above at 0, the indexing for the ith digit is actually starting at 1
print(int(digits[1]) * int(digits[10]) * int(digits[100]) * int(digits[1000]) * int(digits[10000]) * int(digits[100000]) * int(digits[1000000]))
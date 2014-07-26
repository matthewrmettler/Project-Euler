'''
Author: Matthew Mettler
Project Euler, Problem 34
https://projecteuler.net/problem=34

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Status: Correct
'''
factorials = [1]
def init_factorials():
	for i in range(1,10):
		factorials.append(i*factorials[i-1])

init_factorials()
print(sum(x for x in range(10,1000000) if x == sum([factorials[int(y)] for y in str(x)])))
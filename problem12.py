'''
Author: Matthew Mettler
Project Euler, Problem 12
https://projecteuler.net/problem=12

What is the value of the first triangle number to have over five hundred divisors?

Status: Correct
Formula from: http://stackoverflow.com/a/2844920/2227988
References: http://en.wikipedia.org/wiki/Divisor_function
'''
import math

triangle_numbers = [1]
factor_count = [1]

def addTriNum():
	triangle_numbers.append(triangle_numbers[-1] + len(triangle_numbers) + 1)
	#print("Added " + str(triangle_numbers[-1]))
	return

def countFactors(number):
	count = 1
	power = 0
	n = number
	for i in range(2, int(math.ceil(math.sqrt(number)))):
		power = 0
		while n%i == 0:
			n = n / i
			power += 1
		count *= (power+1)
	if n > 1:
		count *= 2
	#print("factors for " + str(number) + ": " + str(count))
	factor_count.append(count)
	return

#main loop
while factor_count[-1] < 500:
	addTriNum()
	countFactors(triangle_numbers[-1])
print(triangle_numbers[-1])
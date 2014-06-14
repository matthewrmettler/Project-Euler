'''
Author: Matthew Mettler
Project Euler, Problem 8
https://projecteuler.net/problem=8

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

Status: Correct
'''

filename = 'problem8_data.txt'
number = []
maxProduct = 0

def checkProduct(index):
	global maxProduct
	product = 1
	for i in range(index,13+index):
		if number[i] == 0:
			return False
		product *= int(number[i])
	maxProduct = max(maxProduct, product)

#read number from file
with open(filename) as f:
	for i in range(0,1020):
		c = f.read(1)
		if c != '\n':
			number.append(c)
del number[-1] #remove eof blank character
print(len(number))

for i in range(0,1000-12):
	checkProduct(i)

print(maxProduct)

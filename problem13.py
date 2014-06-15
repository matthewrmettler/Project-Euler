'''
Author: Matthew Mettler
Project Euler, Problem 13
https://projecteuler.net/problem=13

Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

Status: Correct
Not the best solution in hindsight; still not 'thinking in python'
'''
import math

filename = 'problem13_data.txt'

carry = 0
numbers = []
final_num = []
with open(filename) as f:
	for line in f:
		num = []
		for c in line:
			if c != '\n':
				num.append(c)
		num = num[::-1] #reverse to make addition easier
		numbers.append(num)

print(len(numbers))
print(len(numbers[0]))

for i in range(0, len(numbers[0])): #iterate over every index i
	sum = 0
	for j in range(0, len(numbers)): #sum all values in column j
		sum += int(numbers[j][i])
	sum += carry
	value = sum % 10
	carry = int(math.floor(sum / 10))
	final_num.append(value)
#final carry
while True:
	if carry == 0:
		break
	value = carry % 10
	carry = int(math.floor(carry / 10))
	final_num.append(value)

#reverse
final_num = final_num[::-1]
print(''.join(map(str, final_num[0:10])))


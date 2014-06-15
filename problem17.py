'''
Author: Matthew Mettler
Project Euler, Problem 17
https://projecteuler.net/problem=17

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

Status: Complete, dumb problem
'''
import math
words = { 	
			0: '',
			1: 'one', 
			2: 'two', 
			3: 'three',
			4: 'four',
			5: 'five',
			6: 'six',
			7: 'seven',
			8: 'eight',
			9: 'nine',
			10: 'ten',
			11: 'eleven',
			12: 'twelve',
			13: 'thirteen',
			14: 'fourteen',
			15: 'fifteen',
			16: 'sixteen',
			17: 'seventeen',
			18: 'eighteen',
			19: 'nineteen',
			20: 'twenty',
			30: 'thirty',
			40: 'forty',
			50: 'fifty',
			60: 'sixty',
			70: 'seventy',
			80: 'eighty',
			90: 'ninety',
			100: 'onehundred',
			1000: 'onethousand'
		}

def numCount(num):
	print(num)
	if num in words:
		return len(words[num])
	digits = len(str(num))
	if digits == 2: #tens
		return int(numCount(int(math.floor(num/10))*10) + numCount(num%10))
	if digits == 3: #hundreds
		return int(numCount(int(math.floor(num/100))) + len('hundred') + (0 if num%100==0 else 3+numCount(num%100)))

count = 0
for number in range(1, 1001):
	value = numCount(number)
	print (str(number) + " yields " + str(value))
	count += value
	

print(count)

'''
Author: Matthew Mettler
Project Euler, Problem 38
https://projecteuler.net/problem=38

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the 
concatenated product of an integer with (1,2, ... , n) where n > 1?

Status: Correct
'''

def check_concatenated_product(integer, n):
	prod = "".join([str(integer*i) for i in range(1,n+1)])
	if len(prod) != 9: return False
	if "".join(sorted(list(prod))) != "123456789": return False
	return prod

def main():
	maxVal = 0
	for i in range(3,10000):
		for j in range(2,6):
			if (check_concatenated_product(i,j)):
				maxVal = max(maxVal, check_concatenated_product(i,j))
	print(maxVal)

if __name__ == "__main__":
	main()
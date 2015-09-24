"""
https://projecteuler.net/problem=74

How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
"""

# Rather than calculate it every time, pre-generate the factorials for the digits 0-9
# We can easily reference this too, because x! = factorial_table[x]

factorial_table = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
chain_length = {}

def factorial_digits(num):
	"""Takes an int and sums up the factorial of its digits"""
	return sum([factorial_table[x] for x in map(int, str(num))])


def calculate_chain_length(num, already_seen):
	"""Calculates the chain length of a specific number. This is a recursive function."""
	global chain_length
	
	# Base case #1: Check to see if it's already been calculated.
	if num in chain_length:
		return chain_length[num]

	# It hasn't, so calculate the factorial so that we can check the other two base cases.
	factor = factorial_digits(num)

	#Base case #2: Check to see if it's itself (meaning this value will constantly call itself). Set it's chain to be 1, and return 1.
	if factor == num:
		chain_length[factor] = 1
		return 1

	#Base case #3: We've already seen this factorial coming up, so return 1 to stop the chain here.
	if factor in already_seen:
		return 1

	#We need to do a recursive call now to find the rest of the length. Add this value to the 'already seen' 
	# (so that we don't get stuck in a never-ending loop) and call it again
	already_seen.append(factor)

	# Recursive case, find the chain length of 'factor' and add 1
	chain_length[num] = 1 + calculate_chain_length(factor, already_seen)
	return chain_length[num]


def main():
	#initialize part of chain for recursion to work
	chain_length[0] = 2
	chain_length[1] = 1

	#initialize the count
	count = 0
	for i in range(1000000):
		res = calculate_chain_length(i, [])

		#We're counting the number that equal exactly 60
		if res == 60:
			count += 1
	print(count)

if __name__ == "__main__":
	main()

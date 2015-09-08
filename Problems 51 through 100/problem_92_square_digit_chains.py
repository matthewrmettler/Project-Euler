"""
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 -> 32 -> 13 -> 10 -> 1 -> 1
85 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
Result: Correct, but slow. Just barely didn't achieve the 1 minute limit. 

Not entirely sure how to make this faster. I tried to store chains that failed into a dictionary, so we wouldn't keep calculating failed chains, but that
just made it even slower. I think there's probably a mathematical way to identify what numbers will converge on 1, to just throw them out right away.
i.e. a way to do this problem without actually making the chains and following them.
"""
#pre-calculate all digit squares, in order to cut down on needless calculations
square = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

def sum_digits(n):
    s = 0
    while n:
        s += square[n % 10]
        n /= 10
    return s

def gets_stuck(num):
	"""Returns True if num gets stuck at 89, return False if it gets stuck at 1."""
	result = num
	while (True):
		result = sum_digits(result)
		if result == 89:
			return True
		if result == 1:
			return False

def main():
	count = 0
	for i in range(2, 100000):
		if i % 100000 == 0: print()
		if gets_stuck(i):
			count += 1
	print("Final count: " + str(count))


if __name__ == "__main__":
	main()
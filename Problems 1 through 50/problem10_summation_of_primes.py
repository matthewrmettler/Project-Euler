'''
Author: Matthew Mettler
Project Euler, Problem 10
https://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

Status: Correct
Used Sundaran's Sieve: 
	http://plus.maths.org/content/os/issue50/features/havil/index
'''

def get_primes(max_n):
	numbers = range(3, max_n+1, 2)
	half = (max_n)//2
	initial = 4

	for step in xrange(3, max_n+1, 2):
	    for i in xrange(initial, half, step):
	        numbers[i-1] = 0
	    initial += 2*(step+1)

	    if initial > half:
	        return [2] + filter(None, numbers)

print(sum(get_primes(2000000)))

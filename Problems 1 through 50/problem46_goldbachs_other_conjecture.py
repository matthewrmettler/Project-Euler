'''
Author: Matthew Mettler
Project Euler, Problem 46
https://projecteuler.net/problem=46

It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
Status: Complete

Definitely not efficient. Didn't use sieve, filtered three arrays rather than thinking of efficient ways of getting the smallest values. Still runs in under 4 seconds though!
'''

primes = []
squares = []
odd_composites = []

def gen_primes():
    n = 2
    primes = set()
    while True:
        for p in primes:
            if n % p == 0:
                break
        else:
            primes.add(n)
            yield n
        n += 1


def populate_lists(num):
    global primes
    global squares
    global odd_composites

    gen = gen_primes()
    for i in range(1,num+1):
        primes.append(gen.next())
        squares.append(i*i)
    i = 9
    while(len(odd_composites) < num):
        if i not in primes:
            odd_composites.append(i)
        i += 2

def test_conjecture(num):
    """Tests the conjecture. Returns true if it passes, false if it fails (we want failure)"""
    filtered_squares = filter(lambda x: x < num, squares)
    filtered_primes = filter(lambda x: x < num, primes)
    for sq in filtered_squares:
        test_val = num - 2*sq
        if test_val in filtered_primes:
            return True
    return False

def main():
    populate_lists(5000)
    for item in odd_composites:
        if not test_conjecture(item):
            print item
            return

if __name__ == "__main__":
    main()

'''
Author: Matthew Mettler
Project Euler, Problem 49

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, 
is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 
4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting 
this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
Status: Correct (kinda)

The output is a list of tuples, and you need to dig through it to find [2969, 6299, 9629]. Lots of duplicates.
'''
import itertools
from math import sqrt
primes = []

def is_prime(num):
    for i in range(2, int(sqrt(num)+1)):
        if num % i == 0:
            return False
    return True

def generate_primes():
    global primes
    for i in range(1000,10000):
        if is_prime(i):
            primes.append(i)

def are_permutations(num1, num2, num3):
    """Checks whether three numbers are permutations of each other.

    I turn the numbers to lists via str(num), sort them, and compare the sorts.
    """
    return ( (sorted(list(str(num1))) == sorted(list(str(num2)))) and (sorted(list(str(num2))) == sorted(list(str(num3)))) )

def generate_permutations(num):
    raw_perms = list(itertools.permutations(list(str(num)), 4))
    perms = []
    for item in raw_perms:
        perms.append(''.join(item))
    return list(set(map(int, perms)))

def test_sequence(t):
    diff_1 = t[2]-t[1]
    diff_2 = t[1]-t[0]
    return(diff_2-diff_1 == 0)

def main():
    generate_primes()
    for prime in primes:
        permutations = generate_permutations(prime)
        prime_permutes = filter(lambda x: x in primes, permutations)
        #print(prime_permutes)
        sequences = itertools.permutations(prime_permutes, 3)
        for item in sequences:
            if test_sequence(item):
                print(item)


def test():
    generate_primes()
    permutations = generate_permutations(8147)
    prime_permutes = filter(lambda x: x in primes, permutations)
    #print(prime_permutes)
    sequences = itertools.permutations(prime_permutes, 3)
    for item in sequences:
        if test_sequence(item):
            print(item)

if __name__ == "__main__":
    #test()
    main()
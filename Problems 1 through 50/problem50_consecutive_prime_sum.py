'''
Author: Matthew Mettler
Project Euler, Problem 50

The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, 
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?

Status: Correct, but slow
'''
from math import sqrt
primes = [2]


def is_prime(num):
    if num <= 1: return False
    if num % 2 == 0: return False
    for i in range(3, int(sqrt(num))+2, 2):
        if num % i == 0:
            return False
    return True


def generate_primes():
    global primes
    for i in range(3, 1000001):
        if is_prime(i):
            primes.append(i)


def check_global_prime_sum(primes):
    for i in range(0, len(primes)):
        for j in range(0, i+1):
            if (i-j) == 0:
                pSum = sum(primes[j:])
            else:
                pSum = sum(primes[j:-(i-j)])
            #print(pSum)
            if pSum < 1000000:
                if is_prime(pSum):
                    return pSum
    return 0


def cull_primes(primes):
    """We cull lists of sums from size 2 to 21, since we know the sum needs 
    to be bigger than 21
    """
    for i in range(2,22):
        primes = cull_primes_list(i, primes)
    return primes


def cull_primes_list(value, primes):
    """The largest primes cannot possibly be part of any sum that is smaller 
    than 1000000. So, we look at a value-sized sum of numbers,
    and see which values cannot belong to a sum that large, and delete them.
    """
    for i in range(len(primes)-1, 0, -1):
        if not ((sum(primes[i-value+1:i+1])) >= 1000000):
            #print(primes[i])
            for i in range(len(primes)-1, i, -1):
                del primes[i]
            break
    return primes

def main():
    generate_primes()
    #print(len(primes))
    prime_subset = cull_primes(primes)
    #print(len(prime_subset))
    print(check_global_prime_sum(prime_subset))

def test():
    test = [1,2,3,4,5]

    """
    print test[:]

    print test[0:-1]
    print test[1:]

    print test[0:-2]
    print test[1:-1]
    print test[2:]
    """


if __name__ == "__main__":
    main()
    #test()
'''
Author: Matthew Mettler
Project Euler, Problem 35
https://projecteuler.net/problem=35

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

Status: Complete
'''
from math import sqrt
from collections import deque

circular_primes = [2]

def isPrime(num):
    if num % 2 == 0: 
        return False
    for i in range(3,int(sqrt(num))+2,2):
        if num % i == 0: 
            return False
    return True

def generateCircularPrimes(num):
    """Checks if a number is a circular prime, and appends them all if it is."""
    global circular_primes
    if isPrime(num):

        rotations = get_rotations(num)
        if all(isPrime(x) for x in rotations):
            circular_primes += rotations
        return True
    return False

def get_rotations(num):
    """Rotates a number via the deque library, and returns every rotation."""
    number = list(str(num))
    rotator = deque(number)
    rotations = []

    for i in range(len(number)):
        rotations += [int("".join(rotator))]
        rotator.rotate()

    return rotations

def main():
    for n in range(3, 1000000,2):
        generateCircularPrimes(n)
    print(len(set(circular_primes)))


if __name__ == "__main__":
    main()
'''
Author: Matthew Mettler
Project Euler, Problem 36
https://projecteuler.net/problem=37

The number 3797 has an interesting property. Being prime itself, it is possible 
to continuously remove digits from left to right, and remain prime at each 
stage: 3797, 797, 97, and 7. 
Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to 
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

Status: Correct
'''
from math import sqrt

def is_prime(num):
    if num == 1: return False
    if num == 2: return True
    if num % 2 == 0: return False
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0: return False
    return True

def truncatable(num):
    if not is_prime(num): return False

    num = str(num)
    for i in range(len(num)):
        if not is_prime(int(num[i:])): return False
        if not is_prime(int(num[:i+1])): return False

    return True

def main():
    nums = []
    for i in range(11,1000000,2):
        if truncatable(i):
            nums.append(i)
    print(sum(nums))

if __name__ == "__main__":
    main()
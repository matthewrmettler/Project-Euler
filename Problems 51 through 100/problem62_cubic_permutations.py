'''
Author: Matthew Mettler
Project Euler, Problem 62
https://projecteuler.net/problem=62

The cube, 41063625 (345^3), can be permuted to produce two other cubes: 
56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest 
cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
Status: Correct

Originally I attempted to generate actual permutations of each known i*83, with i = 0..1000.
Too ineffiecient. Then I decided to just generate a stupid amount of primes, all primes from 
0^3 to 100000^3, and just compare them all to each other. Much faster. Took ~25 seconds on my
3 year old laptop.
'''

# Make a dictionary of known cubes, where the key is the length of the cube
# This sorting makes it possible to compare other primes of the same length
known_cubes = {}


def are_permutations(num1, num2):
    """Checks whether two numbers are permutations of each other.

    I turn the numbers to lists via str(num), sort them, and compare the sorts.
    """
    return (sorted(list(str(num1))) == sorted(list(str(num2))))


def populate_base_dict(num):
    """Simple function that initiates all keys in known_cubes to a specific nth cubic number"""
    global known_cubes

    #initialize to empty set
    for i in range(100):
        known_cubes[i] = []

    for i in range(num):
        res = i ** 3
        known_cubes[len(str(res))].append(res)


def main():
    populate_base_dict(100000) # Not sure if I need that many, but it takes so little time anyways
    for l in range(13): #Raised this experimentally, 13 was enough
        for i in range(len(known_cubes[l])):
            count = 1 #Since we're looking for sets that are permutes of each other, include the number itself as the count
            for j in range(i + 1, len(known_cubes[l])):
                if (are_permutations(known_cubes[l][i], known_cubes[l][j])):
                    count += 1
            if count == 5: 
                print("5-pair: {0}".format(known_cubes[l][i]))
                return 0

if __name__ == "__main__":
    main()

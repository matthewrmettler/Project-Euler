'''
Author: Matthew Mettler
Project Euler, Problem 33
https://projecteuler.net/problem=33

Status: Correct
'''
from fractions import Fraction


def check_fraction(numerator, denominator):
    """Checks whether the given numerator, denominator pair can be 
    erroneous 'simplified'"""
    #Needs to be less than one
    if numerator >= denominator:
        return False

    #Convert to arrays
    num_dig = map(int, list(str(numerator)))
    den_dig = map(int, list(str(denominator)))

    # Cross compare digits
    if (num_dig[0] == den_dig[0]) and (num_dig[0] != 0) and (den_dig[1] != 0):
        if (numerator/float(denominator)) == (num_dig[1]/float(den_dig[1])):
            return True

    if (num_dig[0] == den_dig[1]) and (num_dig[0] != 0) and (den_dig[0] != 0):
        if (numerator/float(denominator)) == (num_dig[1]/float(den_dig[0])):
            return True

    if (num_dig[1] == den_dig[0]) and (num_dig[1] != 0) and (den_dig[1] != 0):
        if (numerator/float(denominator)) == (num_dig[0]/float(den_dig[1])):
            return True

    if (num_dig[1] == den_dig[1]) and (num_dig[1] != 0) and (den_dig[0] != 0):
        if (numerator/float(denominator)) == (num_dig[0]/float(den_dig[0])):
            return True

    return False

def main():
    fractions = []

    #Try every possible fraction, out of all ~1000
    for i in range(10,101):
        for j in range(10,101):
            if (check_fraction(i, j)):
                fractions.append((i,j))

    #Take the four tuples, and do the math needed to get the denominator 
    # of the product of the four fractions in simplest terms
    print(Fraction(reduce(lambda x,y:x*y,[Fraction(x[0], x[1]) for x in fractions])))

if __name__ == "__main__":
    main()

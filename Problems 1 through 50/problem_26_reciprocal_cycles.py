'''
Author: Matthew Mettler
Project Euler, Problem 26
https://projecteuler.net/problem=26
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
Status: Complete
Used the fact that you can look at cycles in the remainder of the digits to find 
cycles in the digits to solve
'''

def remainder_length(num):
    value = 1
    remainders = []

    while(True):
        result = value % num
        if result in remainders:
            break
        remainders.append(result)
        value = result*10

    return len(remainders)

def main():
    max_res = 0
    max_num = 0
    for i in range(2, 1000):
        if remainder_length(i) > max_res:
            max_res = remainder_length(i)
            max_num = i
    print(max_num, max_res)

if __name__ == "__main__":
    main()
'''
Author: Matthew Mettler
Project Euler, Problem 28
https://projecteuler.net/problem=28

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
Status: Corrent

This is an Ulam spiral!

You can figure out the value of the four corners of a 'layer' by using the dimensions of that layer (nxn) and some math related to the
n-1th layer. Basically, the value of the top-right corner of the (n-1)th layer is always (n-1)^2. Then, for the nth layer's bottom right,
it's just (n-1) more numbers after that (since the next layer starts one down from the top right corner). Then, each additional corner is n-1
steps after that corner. Repeat for every layer.
'''


center = 1
diagonals = [1]
def build_layer(n):
    global diagonals
    bottom_right = (n-2)*(n-2)+(n-1)
    bottom_left = bottom_right + (n-1)
    top_left = bottom_left + (n-1)
    top_right = n*n
    diagonals += [bottom_left, bottom_right, top_left, top_right]

def main():
    for i in range(3,1002, 2):
        build_layer(i)
    print(sum(diagonals))

if __name__ == "__main__":
    main()
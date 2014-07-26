'''
Author: Matthew Mettler
Project Euler, Problem 25
https://projecteuler.net/problem=25

What is the first term in the Fibonacci sequence to contain 1000 digits?

Status: Correct
'''
fibonacci = [1,1]

def genFib():
	fibonacci.append(fibonacci[-1] + fibonacci[-2])

while (len(str(fibonacci[-1])) != 1000): genFib()

print(len(fibonacci))
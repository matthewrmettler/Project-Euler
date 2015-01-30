'''
Author: Matthew Mettler
Project Euler, Problem 39
https://projecteuler.net/problem=39

If p is the perimeter of a right angle triangle with integral length sides,
 {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?

Status: Incomplete
'''
pVal = 0
max = 0

for perimeter in range(1001):
	#if (perimeter%20==0): print("checking p="+str(perimeter))
	num = 0
	for b in range(perimeter):
		for c in range(perimeter-b):
			a = perimeter-b-c
			if (a*a + b*b == c*c):
				num += 1
	if num > max: 
		max = num
		pVal = perimeter

print(pVal)
#print(max)
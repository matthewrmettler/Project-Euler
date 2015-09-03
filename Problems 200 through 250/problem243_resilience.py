'''
Author: Matthew Mettler
Project Euler, Problem 243
https://projecteuler.net/problem=81

Find the smallest denominator d, having a resilience R(d) < 15499/94744 .

Status: Incomplete
'''

def hcf( n1, n2 ):
  while n1*n2:
    if n1 > n2:
      n1 %= n2
    else:
      n2 %= n1
  return max( n1, n2 )

def is_coprime(a,b):
	return hcf( a, b ) == 1

def get_resil(n):
	count = 0.0
	for i in range(n):
		if is_coprime(i,n): count += 1.0
	if (n % 100 == 0): print(str(n) + " - " + str(float(count / float(n))))
	return float(count / float(n))

goal = float(15499.0/94744.0)
print(goal)
start = 3
print(start)
while(get_resil(start)) >= goal:
	#if (start % 33 == 0): print(start)
	start += 1
print(start)
'''
Author: Matthew Mettler
Project Euler, Problem 45
https://projecteuler.net/problem=45

It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
Status: Correct. Program runs for a while, but you can simpyl cancel it once it spits
out the number after 40755.
'''
tris = {}
pentas = {}
hexas = {}

def initialize_dicts():
	for i in range(1,25):
		tris[i] = []
		pentas[i] = []
		hexas[i] = []

def generate_triangle(n):
	return n*(n+1)/2

def generate_pentagonal(n):
	return n*(3*n-1)/2

def generate_hexagonal(n):
	return n*(2*n-1)

def check_for_matches():
	for length in tris.keys():
		for item in tris[length]:
			if item in pentas[length]:
				if item in hexas[length]:
					print(item)
	"""
	for i in range(1,10):
		for t in tris[i]:
			for p in pentas[i]:
				for h in hexas[i]:
					if t == p == h:
						print(t)
						"""
def main():
	initialize_dicts()

	for i in range(1,100000):
		t = generate_triangle(i)
		p = generate_pentagonal(i)
		h = generate_hexagonal(i)

		tris[len(str(t))].append(t)
		pentas[len(str(p))].append(p)
		hexas[len(str(h))].append(h)

	#print(tris)
	#print(pentas)
	#print(hexas)

	check_for_matches()
	#print(tris)

if __name__ == "__main__":
	main()
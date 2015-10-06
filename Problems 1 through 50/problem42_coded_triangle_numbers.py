'''
Author: Matthew Mettler
Project Euler, Problem 42
https://projecteuler.net/problem=42

The nth term of the sequence of triangle numbers is given by, t_n = n(n+1)/2; 
so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical 
position and adding these values we form a word value. For example, the word 
value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number 
then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file 
containing nearly two-thousand common English words, how many are triangle words?

Status: Correct
'''

triangle_num = []

def generate_triangluar_numbers():
	global triangle_num
	for i in range(1,101):
		triangle_num.append(i*(i+1)/2)

def calculate_triangular_value(word):
	value = 0
	for letter in word:
		value += (ord(letter) - ord('a')+1)
	return value

def main():
	generate_triangluar_numbers()
	count = 0
	with open("problem42_data.txt", "r") as f:
		data = f.readline().split(",")
		for word in data:
			word = word.strip("\"").lower()
			if calculate_triangular_value(word) in triangle_num:
				count += 1
	print(count)

if __name__ == "__main__":
	main()
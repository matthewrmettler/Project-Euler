'''
Author: Matthew Mettler
Project Euler, Problem 31
https://projecteuler.net/problem=31

How many different ways can 2 pounds be made using any number of coins?

Status: Complete, recursive solution
Correct according to https://code.google.com/p/projecteuler-solutions/wiki/ProjectEulerSolutions
[Finished in 0.1s]
'''
coins = [1, 2, 5, 10, 20, 50, 100, 200]
coins = coins[::-1]
init_target = 200

def coinsNum(num, target):
	#print("CoinsNum with %d, %d" % (coins[num], target))
	count = 0
	if target == 0 : return 1
	if coins[num] == 1: return 1
	ways = target / coins[num]
	for i in range(ways, -1, -1):
		count += coinsNum(num+1, target-i*coins[num])
	return count

print(coinsNum(0, init_target))
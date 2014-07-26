'''
Author: Matthew Mettler
Project Euler, Problem 19
https://projecteuler.net/problem=19

You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
Status: Correct
'''
twentieth_century = []
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(100):
	year = []
	for month in months:
		year.append([0]*month)
	twentieth_century.append(year)

for year in range(1901, 2001):
	if year % 4 == 0:
		twentieth_century[year-1901][1] = [0]*29

#0 is sunday; 1901 begins on a tuesday
day_of_week = 2 
count = 0
for year in range(len(twentieth_century)):
	for month in range(len(twentieth_century[year])):
		for day in range(len(twentieth_century[year][month])):
			twentieth_century[year][month][day] = day_of_week
			if day == 0 and day_of_week == 0: count += 1
			day_of_week = (day_of_week+1) % 7

print(count)
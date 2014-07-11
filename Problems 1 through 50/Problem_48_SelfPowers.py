'''
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
Status: Correct
'''
print(str(sum([int(str(value**value)[-10:]) for value in range(1, 1001)]))[-10:])
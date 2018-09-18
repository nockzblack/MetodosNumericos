"""
Return the Factorial
Create a function that takes an integer and returns the factorial of that integer. That is, the integer multiplied by all positive lower integers.
Examples
3 ➞ 6

5 ➞ 120

13 ➞ 6227020800
Notes
Assume all inputs are >= 0.
0! = 1.
"""

def factorial(num):
	if(num == 0):
		return 1
	else:
		return num *factorial(num-1)
    
    
    
"""
Absolutely Sum
Take a list of integers (positive or negative or both) and return the sum of the absolute value of each element.
Examples
[2, -1, 4, 8, 10] ➞ 25

[-3, -4, -10, -2, -3] ➞ 22

[2, 4, 6, 8, 10] ➞ 30

[-1] ➞ 1
"""

def get_abs_sum(lst):
	sum = 0
	for i in lst:
		sum += abs(i)
	
	return sum

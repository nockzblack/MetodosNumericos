"""
Eliminate Odd Numbers within a List
Published by Sri in Python
algorithmsarraysmathnumbersvalidation
Create a function that takes a list of numbers and returns only the even values.
Examples
[1, 2, 3, 4, 5, 6, 7, 8] ➞ [2, 4, 6, 8]

[43, 65, 23, 89, 53, 9, 6] ➞ [6]

[718, 991, 449, 644, 380, 440] ➞ [718, 644, 380, 440]
"""

def noOdds(lst):
	auxArr = []
	for elem in lst:
		if elem % 2 == 0:
			auxArr.append(elem)
			
	return auxArr
	


"""
Find the Smallest Number in a List
Published by Sri in Python
arraysloopsnumberssorting
Create a function that takes a list of numbers and returns the smallest number in the list.
Examples
[34, 15, 88, 2] ➞ 2

[34, -345, -1, 100] ➞ -345

[-76, 1.345, 1, 0] ➞ -76

[0.4356, 0.8795, 0.5435, -0.9999] ➞ -0.9999

[7, 7, 7] ➞ 7
"""

def findSmallestNum(lst):
	min = lst[0]
	for elem in lst:
		if elem < min:
			min = elem
			
	return min
  
  
"""
Is the Number Even or Odd?
Published by Matt in Python
algorithmsmathnumbersvalidation
Create a function that takes a number as an argument and returns "even" for even numbers and "odd" for odd numbers.
Examples
3 ➞ "odd"

146 ➞ "even"

19 ➞ "odd"
"""

def isEvenOrOdd(num):
	if num % 2 == 0:
		return "even"
	else:
		return "odd"
	


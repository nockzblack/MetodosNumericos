"""
Find the Minimum, Maximum, Length and Average Values
Published by GlassToeStudio in Python

Create a function that takes a list of numbers and returns the following statistics:
Minimum Value
Maximum Value
Sequence Length
Average Value

Examples
[6, 9, 15, -2, 92, 11] ➞ [-2, 92, 6, 21.833333333333332]

[30, 43, 20, 92, 3, 74] ➞ [3, 92, 6, 43.666666666666664]

[4.54, 8.32, 5.20] ➞ [4.54, 8.32, 3, 6.02]

"""

def minMaxLengthAverage(lst):
	min = lst[0]
	max = lst[0]
	sum = 0
	
	for i in lst:
		sum += i
		if i < min:
			min = i
		if i > max:
			max = i
	
	
	average = sum/len(lst)
	
	return [min, max, len(lst), average]
  
  
  
  
"""
Filter out Strings from an Array
Published by Sri in Python
Create a function that takes a list of non-negative numbers / strings and returns a new list without the strings.
Example
[1, 2, "a", "b"] ➞ [1, 2]

[1, "a", "b", 0, 15] ➞ [1, 0, 15]

[1, 2, "aasf", "1", "123", 123] ➞ [1, 2, 123]
"""

def filter_list(lst):
	auxLst = []
	for i in lst:
		if type(i) is int:
			auxLst.append(i)
			
	return auxLst
  
  
  """
Remove Duplicates from List
Published by Sri in Python

Create a function that takes a list of items, removes all duplicate items and returns a new list in the same sequential order as the old list (minus duplicates).
Examples
["John", "Taylor", "John"] ➞ ["John", "Taylor"]

[1, 0, 1, 0] ➞ [1, 0]

['The', 'big', 'cat'] ➞ ['The', 'big', 'cat']
  """
  
  def removeDups(lst):
	auxLst = []
	
	for i in lst:
		if i not in auxLst:
			auxLst.append(i)
			
	return auxLst
			

def cumulative_sum(lst):
    auxLst = []
    for i in range(len(lst)):
        if i>0:
            auxLst.append(auxLst[-1]+ lst[i])
        else:
            auxLst.append(lst[i])
    return auxLst
    
    
    
def minMaxLengthAverage(lst):
  auxLst = []
	auxLst.append(min(lst))
	auxLst.append(max(lst))
	auxLst.append(len(lst))
	auxLst.append((sum(lst))/c)
	return auxLst
  
  
  def sum_two_smallest_nums(lst):
  lst.sort()
  for i in range(len(lst)):
    if (lst[i] >=0):
      return lst[i]+lst[i+1]

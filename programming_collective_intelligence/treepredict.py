my_data=[['slashdot','USA','yes',18,'None'],
['google','France','yes',23,'Premium'],
['digg','USA','yes',24,'Basic'],
['kiwitobes','France','yes',23,'Basic'],
['google','UK','no',21,'Premium'],
['(direct)','New Zealand','no',12,'None'],
['(direct)','UK','no',21,'Basic'],
['google','USA','no',24,'Premium'],
['slashdot','France','yes',19,'None'],
['digg','USA','no',18,'None'],
['google','UK','no',18,'None'],
['kiwitobes','UK','no',19,'None'],
['digg','New Zealand','yes',12,'Basic'],
['slashdot','UK','no',21,'None'],
['google','UK','yes',18,'Basic'],
['kiwitobes','France','yes',19,'Basic']]


class decisionnode:
def __init_ _(self,col=-1,value=None,results=None,tb=None,fb=None):
self.col=col
self.value=value
self.results=results
self.tb=tb
self.fb=fb


# Create counts of possible results (the last column of
# each row is the result)
def uniquecounts(rows):
results={}
for row in rows:
# The result is the last column
r=row[len(row)-1]
if r not in results: results[r]=0
results[r]+=1
return results

# Divides a set on a specific column. Can handle numeric
# or nominal values
def divideset(rows,column,value):
# Make a function that tells us if a row is in
# the first group (true) or the second group (false)
split_function=None
if isinstance(value,int) or isinstance(value,float):
split_function=lambda row:row[column]>=value
else:
split_function=lambda row:row[column]==value
# Divide the rows into two sets and return them
set1=[row for row in rows if split_function(row)]
set2=[row for row in rows if not split_function(row)]
return (set1,set2)
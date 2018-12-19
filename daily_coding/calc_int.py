def check_values(datalist):
	for value in datalist:
		if type(value) == 'string':
			return False
	return True

def multiply_list(datalist):
	result = 1
	for value in datalist:
		result = result * value
	return result

def calc_data(value, datalist):
	templist = datalist
	templist.pop(value)
	return multiply_list(templist)
	
	
	
def calc_int(datalist):
	if len(datalist) < 1:
    return "Cannot calculate - Empty list"
  else:
    return calc_data(datalist)
		#if check_values(datalist) == True:
		#	return "Inconsistent data types in list"
		#else:

			
		

def main():
  datalist = [1,2,3,4,5]
  print(calc_int(datalist))
	#datalist = []
	#assert calc_int(datalist) == "Cannot calculate - Empty list", "Issue"
	#datalist = [1,2,3,4,5]
  #print(calc_int(datalist))
	#assert cmp(calc_int(datalist),[120,60,40,30,24]) == 1, "Issue"
	#datalist = [3,2,1]
	#assert cmp(calc_int(datalist),[2,3,6])==1, "Issue"
	#datalist = ["a",3,2]
	#assert calc_int(datalist) == "Inconsistent data types in list","Issue"

	
if __name__ == "__main__":
	main()
	

def check_values(datalist):
	for value in datalist:
		if type(value) == str:
			return False
	return True

def multiply_list(datalist):
	result = 1
	for value in datalist:
		result = result * value
	return result

def calc_data(value, listdata):
	templist = []
	for i in range(0,len(listdata)):
		if i != value:
			templist.append(listdata[i])
	return multiply_list(templist)
	

def calc_int(listinfo):
	if len(listinfo) < 1:
		return []
	elif check_values(listinfo) == False:
		return []
  	else:
  		outputlist = []
  		for i in range(0,len(listinfo)):
  			outputlist.append(calc_data(i,listinfo))
  	return outputlist


def main():
  datalist = [1,2,3,4,5] #[120,60,40,30,24]
  print(calc_int(datalist))
  datalist = [3,2,1]
  print(calc_int(datalist)) #[2,3,6]
  datalist = []
  print(calc_int(datalist))
  datalist = ["a",3,2]
  print(calc_int(datalist))
	
if __name__ == "__main__":
	main()
	

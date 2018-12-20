#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

def calc_data(val, value, listdata):
	templist = []
	for data in listdata:
		if data != val:
			templist.append(data)
	
	for temp in templist:
		if temp + val == value:
			return True
	return False

def calc_check(value,alist):
	templist = []
	for val in alist:
		if calc_data(val,value,alist) == True:
			templist.append(val)
	return templist

def main():
	datalist = [10,15,3,7]
	kvalue = 17
	print(calc_check(kvalue,datalist))


if __name__ == "__main__":
	main()
#assume array is already sorted if not empty

def binary_search_random(key,ary):
	begin = 0
	end = len(ary)-1
	mid = (begin + end)//2
	found = False
	if key == ary[mid]:
		found = True
	elif key < ary[mid]:
		newary = ary[:mid]
		if key in newary:
			found = True
	else:
		newary = ary[mid + 1:]
		if key in newary:
			found = True
	retrun found

def binary_search_recur(key,ary):
	begin = 0
	end = len(ary)-1
	mid = (begin + end)//2
	found = False
	while (begin <=end and not found):
		if key == ary[mid]:
			found = True
		elif key < ary[mid]:
			return binary_search_recur(key,ary[:mid])
		else:
			return binary_search_recur(key,ary[mid+1:])
	return found

def binary_search_iter(key,ary):
	begin = 0
	end = len(ary)-1
	mid = (begin + end)//2
	found = False
	while (begin <=end and not found):
		if key == ary[mid]:
			found = True
		elif key < ary[mid]:
			end = mid - 1
		else:
			begin = mid + 1
	return found


def binary_search(items, desired_item, start=0, end=None):
    if end == None:
        end = len(items)

    if start == end:
        raise ValueError("%s was not found in the list." % desired_item)

    pos = (end - start) // 2 + start

    if desired_item == items[pos]:
        return pos
    elif desired_item > items[pos]:
        return binary_search(items, desired_item, start=(pos + 1), end=end)
    else:
        return binary_search(items, desired_item, start=start, end=pos)

def main():
	print("check algorithms")

if __name__ == "__main__":
	main()
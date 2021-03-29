# algorithm merge sort
# function merge_two_lists() should unite two lists
def merge_two_lists(a:[list], b:[list]):
	l = []
	# i and j are pointers to the elements of the list 
	i = j = 0
	while i<len(a) and j<len(b):
		if a[i]<b[j]:
			l.append(a[i])
			i+=1
		else:
			l.append(b[j])
			j+=1 
	if i<len(a):
		l += a[i:]
	if j<len(b):
		l += b[j:]
	return l

# main sorting function
def merge_sort(s):
	# base case for recursioon
	if len(s) == 1:
		return s
	middle = len(s)//2
	left = merge_sort(s[:middle])
	right = merge_sort(s[middle:])
	return merge_two_lists(left, right)

list_of_num = [7,5,2,3,9,8,6]
print(f"unsorted list: {list_of_num}")
print(f"sorted list: {merge_sort(list_of_num)}")



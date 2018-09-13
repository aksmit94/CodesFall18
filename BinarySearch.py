#Binary Search
##Inputs: Left inclusive & Right exclusive
##Initial call: BinarySearch(a,0,len(a),p)
def BinarySearch(a, left, right, p):
	#Define middle position
	mid = (left + right)//2
	
	#If element is found
	if(a[mid - 1] == p):
		print ("Index of {} is {}".format(p,mid-1))
		return 
	
	#If element not found and all elements checked
	elif(left > right):
		print("Element not found in the list")
		return
		
	#If middle element is greater than p, search left array
	elif(a[mid - 1] > p):
		##Condition to make sure recursion ends when p < a[0]
		if(mid == left):
			right = mid - 1
		else:
			right = mid
	
	#If middle element is lesser than p, search right array
	elif(a[mid - 1] < p):
		left = mid + 1
		
	#Recursive call
	BinarySearch(a, left, right, p)	

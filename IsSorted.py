def IsSorted(arr):
	n = len(arr)
	for i in range(n - 1):
		if(arr[i] > arr[i+1]):
			break
		else:
			continue
	
	if(i < n - 2):
		print ("Array is not sorted")
	else:
		print ("Array is sorted")
		
	
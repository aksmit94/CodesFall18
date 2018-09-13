#Quick Sort

##Inputs: Left inclusive & Right exclusive
##Initial call:QuickSort(a,0,len(a))
def WhileLoop_QuickSort(a, left, right):

	#Termination condition
	if(right < left + 1):
		return
	else:
		#Set pivot element - always choose last element as pivot
		pivot = right - 1
		
		#Call Partition
		split = WhileLoop_Partition(a, left, right, pivot)
		
		#Recursive calls
		WhileLoop_QuickSort(a, left, split)
		WhileLoop_QuickSort(a, split+1, right)
	
def WhileLoop_Partition(a, left, right, pivot):
	
	##Following the general convention of breaking array into 3 partitions (apart from pivot): [[i]...[split]**[split+1]...[j]**[j+1]...**[pivot]]
	##elements less than pivot -> i to split --- SmallArr partition
	##elements greater than pivot -> split + 1 to j --- LargeArr partition
	## elements yet to be examined -> j + 1 to pivot - 1 (because pivot is last element) --- UnexaminedArr partition
	##Comparisons will be done between a[j+1] and the pivot element
	#Initializations
	i = left - 1
	split = i
	j = left - 1
	
	while(j < pivot - 1):
	
		#Comparing pivot to a[i]
		##If a[j+1] > pivot, do nothing
		if(a[pivot] < a[j + 1]):
			j = j + 1
		
		##If a[i] < pivot, perform 3 steps
		elif(a[pivot] > a[j + 1]):
		
			##Step 1: swap j+1 element with start of region with elements > pivot element i.e. element at index split+1
			temp = a[split + 1]
			a[split + 1] = a[j+1]
			a[j+1] = temp
			
			##Step 2: increment split by 1
			split = split + 1
			
			##Step 3: increment j by 1 (j is the last element of LargeArr partition)
			##########Since we just put the first element from this partition to the last, we need to increment index value of last element i.e. j
			j = j + 1
	
	#Place pivot element at correct (index = split) position:
	##Done by swapping pivot element with first element of LargeArr partition
	temp = a[split + 1]
	a[split + 1] = a[pivot]
	a[pivot] = temp
	
	return split + 1
#Merge Sort
import sys
##Left = 0; Right = len(a)
def MergeSort(a, left, right):
	#If array size = 1, do nothing
	if(left == right - 1):
		return
	else:
		#define middle element index
		mid = (left + right) // 2
		
		#Recursive calls
		MergeSort(a, left, mid)
		MergeSort(a, mid, right)
		Merge(a, left, mid, right)

def Merge(a,left, mid, right):
	#define left and right halves
	LeftHalf = a[slice(left, mid)]
	RightHalf = a[slice(mid, right)]
	
	#Sentinals - to facilitate finding list end
	LeftHalf.append(sys.maxsize)
	RightHalf.append(sys.maxsize)
	
	#Pointers to left and right halves
	l = 0
	r = 0
		
	for i in range(left, right):
		if(LeftHalf[l] < RightHalf[r]):
			a[i] = LeftHalf[l]
			l +=1
		else:
			a[i] = RightHalf[r]
	
			r += 1
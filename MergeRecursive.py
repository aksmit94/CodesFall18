# def Merge(a,left, mid, right):
	# #define left and right halves
	# LeftHalf = a[slice(left, mid)]
	# RightHalf = a[slice(mid, right)]
	
	# #Sentinals - to facilitate finding list end
	# LeftHalf.append(sys.maxsize)
	# RightHalf.append(sys.maxsize)
	
	# #Pointers to left and right halves
	# l = 0
	# r = 0
		
	# for i in range(left, right):
		# if(LeftHalf[l] < RightHalf[r]):
			# a[i] = LeftHalf[l]
			# l +=1
		# else:
			# a[i] = RightHalf[r]
			# r += 1
	

#Merge Routine (Recursive)
import sys

def Merge(a, left, mid, right):
	#define left and right halves
	LeftHalf = a[slice(left, mid)]
	RightHalf = a[slice(mid, right)]
	
	#Sentinals - to facilitate finding list end
	# LeftHalf.append(sys.maxsize)
	# RightHalf.append(sys.maxsize)
	
	
	
	if(len(LeftHalf) == 1 || len(RightHalf) == 1):
		if(LeftHalf[0] < RightHalf[0]):
			a[left] = LeftHalf[0]
		else:
			a[left] = RightHalf[0]
	else:
		return Merge(a, left + 1, mid, right - 1)
	
	# for i in range(left, right):
		# if(LeftHalf[l] < RightHalf[r]):
			# a[i] = LeftHalf[l]
			# l +=1
		# else:
			# a[i] = RightHalf[r]
			# r += 1
	
	
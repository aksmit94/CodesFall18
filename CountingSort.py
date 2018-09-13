##Counting Sort 
import numpy as np;

def CSort(a):
	
	#extract length of input
	length = a.max() + 1;
	
	#Create array of that 'length'
	counts = np.zeros(length);
	
	for i in range(len(a)):
		val = a[i];
		counts[val] += 1;
		
	sorted = np.zeros(len(a));
	p = 0;
	
	for k in range(length):
			while(counts[k] > 0):
				sorted[p] = k;
				counts[k] -= 1;
				p += 1;
		
	return sorted;

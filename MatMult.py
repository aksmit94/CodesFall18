#Matrix Multiplication - the normie way
##Following method is O(n^3)
import numpy as np
def MatMult(a, b, c, n):
	
	prod = np.zeros((n,n))
	
	##Calculating Product
	for i in range(0,n):
		for j in range(0,n):
			for k in range(0,n):
				prod[i,j] += a[i,k]*b[k,j]
			
			if(c[i,j] != prod[i,j]):
				return 'Matrix Product not correct'
			else:
				continue
	return "Matrix product correct"
	
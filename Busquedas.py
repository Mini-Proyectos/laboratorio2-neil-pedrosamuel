def InsertSort(A, p, r):
	for j in range(p+1,r):
		key = A[j]
		i=j-1
		while(i>=p and A[i]>key):
			A[i+1] = A[i]
			i = i - 1
		A[i+1] = key
	return A
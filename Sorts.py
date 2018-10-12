import sys

def MergeSort(A, p, r):
	if(p<r):		
		mid=(p+r)//2
		MergeSort(A,p,mid)
		MergeSort(A,mid+1,r)
		Merge(A,p,mid,r) 

def Merge(A, p, mid, r):
	n = mid - p + 1 
	m = r - mid
	L = [0] * n			
	R = [0] * m
	for i in range(0,n): 
 		L[i] = A[p+i]
	for j in range(0,m):
		R[j]=A[mid+1+j]
	i = 0
	j = 0
	k=p
	while(i<n and j<m):
		if (L[i] <= R[j]):
			A[k] = L[i]
			i=i+1
		else:
			A[k]= R[j]
			j=j+1
		k = k+1

	while i<n:
		A[k]=L[i]
		i=i+1
		k=k+1
	while j<m:
		A[k]=R[j]
		j=j+1
		k=k+1

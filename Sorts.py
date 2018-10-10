import sys

def MergeSort(A, l, r):
	if(l<r):		
		mid=(l+r)//2
		MergeSort(A,l,mid)
		MergeSort(A,mid+1,r)
		Merge(A,l,mid,r) 

def Merge(A, l, mid, r):
	n = mid - l + 1 
	m = r - mid
	L = [0] * n			
	R = [0] * m
	for i in range(0,n): 
 		L[i] = A[l+i]
	for j in range(0,m):
		R[j]=A[mid+1+j]
	i = 0
	j = 0
	k=l
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

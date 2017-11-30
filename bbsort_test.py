a = [1,3,4,23,54,2,6,57,8,8,8,34,7,3,6,8,10]

def bbsort(A):
	for i in range(len(A)-1, 0, -1):
		for j in range(i):
			if A[j]>A[j+1]:
				temp = A[j]
				A[j] = A[j+1]
				A[j+1] = temp
	return A

print(bbsort(a))
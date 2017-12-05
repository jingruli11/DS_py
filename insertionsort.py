def insertionSort(ll):
	for i in range(len(ll)):
		key = ll[i]
		j = i-1
		while j >= 0 and ll[j] > key:
			ll[j+1] = ll[j]
			j -= 1
		ll[j+1] = key
	return ll


mylist=[12,23,54,2,4,7,3,7,9,4,7,9,32]

print(insertionSort(mylist))
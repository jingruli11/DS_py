
#def selectionSort(ll):
#	for i in range(len(ll)):
#		k = i
#		for j in range(i + 1, len(ll)):
#			if ll[k] < ll[j]:
#				k = j
#			if k != j:
#				temp = ll[j]
#				ll[j] = ll[k]
#				ll[k] = temp
#	return ll

#mylist=[23,54,2,4,7,3,7,9,4,7,9,32]

#print(selectionSort(mylist))

def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp

   return alist

mylist=[23,54,2,4,7,3,7,9,4,7,9,32]

print(selectionSort(mylist))
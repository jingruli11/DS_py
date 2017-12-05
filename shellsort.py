def insertionSort(ll):
	for i in range(len(ll)):
		key = ll[i]
		j = i-1
		while j >= 0 and ll[j] > key:
			ll[j+1] = ll[j]
			j -= 1
		ll[j+1] = key
	return ll


def shellSort(ll):
	gap = len(ll)/2
	while gap > 0:



standup

did:
- 5 differnet types of charts, successfully developed 4 new looks, one for each type
- specified looks to be done in this sprint for shilpa

do:
- propose a meeting with jay and anh to talk about dimension and measure needed (percentage, region)
- ask anh to share his region map chart

block:
- region dimension string --> location type (necessary for this sprint)
- percentage measure (not necessary for this sprint)
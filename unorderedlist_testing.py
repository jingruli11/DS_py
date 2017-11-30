from Node import Node
from UnorderedList import UnorderedList

mylist = UnorderedList()

mylist.add(3)
print(mylist.isEmpty())

mylist.add(2)
mylist.add(12)
mylist.add(123)
mylist.add(18)
mylist.add(73)

print(mylist.size())

print(mylist.search(123))
print(mylist.search(19))

print(mylist.size())

mylist.remove(2)
print(mylist.size())
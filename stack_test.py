from Stack import Stack

s = Stack()

print(s.isEmpty())
s.push('crazy')
print(s.isEmpty())
s.pop()
print(s.isEmpty())
s.push(21)
s.push(4)
print(s.size())
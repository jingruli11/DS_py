from Queue import Queue

q = Queue()

print(q.isEmpty())
q.enqueue('whisper')
q.enqueue('careless')
print(q.isEmpty())
print(q.size())
q.dequeue()
print(q.size())
print(q.dequeue())
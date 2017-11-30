from BinaryTree import BinaryTree

r = BinaryTree('a')
print(r.getRootVal())

print(r.getLeftChild())

r.insertLeft('b')
print(r.getLeftChild())
print(r.getRootVal())

r.insertRight('c')
print(r.getRightChild())
print(r.getRightChild().getRootVal())

r.getRightChild().setRootVal('not today')
print(r.getRightChild().getRootVal())
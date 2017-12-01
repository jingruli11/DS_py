import operator
from BinaryTree import BinaryTree

def preorder(tree):
	if tree:
		print(tree.getRootVal())
		preorder(tree.getLeftChild())
		preorder(tree.getRightChild())

def postorder(tree):
	if tree != None:
		postorder(tree.getLeftChild())
		postorder(tree.getRightChild())
		print(tree.getRootVal())

def postordereval(tree):
	opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/':operator.truediv}
	res1 = None
	res2 = None
	if tree:
		res1 = postordereval(tree.getLeftChild())
		res2 = postordereval(tree.getRightChild())
		if res1 and res2:
			return opers[tree.getRootVal()](res1, res2)
		else:
			return tree.getRootVal()

def inorder(tree):
	if tree:
		inorder(tree.getLeftChild())
		print(tree.getRootVal())
		inroder(tree.getRightChild())


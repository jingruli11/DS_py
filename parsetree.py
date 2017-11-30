import operator
from BinaryTree import BinaryTree
from Stack import Stack

def buildParseTree(mm):
	mmlist = mm.split()
	pstack = Stack()
	eTree = BinaryTree('')
	pstack.push(eTree)
	currentTree = eTree

	for i in mmlist:
		if i == '(':
			currentTree.insertLeft('')
			pstack.push(currentTree)
			currentTree = currentTree.getLeftChild()
		elif i not in ['+', '-', '*', '/']:
			currentTree.setRootVal(i)
			parent = pstack.pop()
			currentTree = parent
		elif i in ['+', '-', '*', '/']:
			currentTree.setRootVal(i)
			currentTree.insertRight('')
			pstack.push(currentTree)
			currentTree = currentTree.getRightChild()
		elif i == ')':
			currentTree = pstack.pop()
		else:
			raise ValueError
	return eTree

pt = buildParseTree("((10+5)*3)")

def evaluate(parsetree):
	opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
	leftC = parsetree.getLeftChild()
	rightC = parsetree.getRightChild()

	if leftC and rightC:
		fn = opers[parsetree.getRootVal()]
		return fn(evaluate(leftC), evaluate(rightC))
	else:
		return parsetree.getRootVal()

print(evaluate(pt))

from binarytree import BinaryTree
import operator

def binaryparsertree(expr):
    exp = expr.split()
    pStack = []
    eTree = BinaryTree('')
    pStack.append(eTree)
    currentTree = eTree
    for i in exp:
        if i == '(':
            currentTree.addLeft('')
            pStack.append(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '/', '*', ')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '/', '*']:
            currentTree.setRootVal(i)
            currentTree.addRight('')
            pStack.append(currentTree)
            currentTree = currentTree.getRightChild()

        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree


def evaluate(parserTree):
    mapper = {
        '+': operator.add,
        '-': operator.sub,
        '/': operator.div,
        '*': operator.mul,
    }

    if parserTree.getLeftChild() and parserTree.getRightChild():
        fn = mapper[parserTree.getRootVal()]
        return fn(evaluate(parserTree.getLeftChild()), evaluate(parserTree.getRightChild()))    
    else:
        return parserTree.getRootVal()

def printexpr(parserTree):
    str1 = ''
    if parserTree is not None:
        str1 =  '(' + printexpr(parserTree.getLeftChild())
        str1 = str1 + str(parserTree.getRootVal())
        str1 = str1 + printexpr(parserTree.getRightChild()) + ')'
    return str1

def preorder(parserTree):
    str1 = ''
    if parserTree:
        str1 = '(' + str(parserTree.getRootVal())
        str1 = str1 + preorder(parserTree.getLeftChild())
        str1 = str1 + preorder(parserTree.getRightChild()) + ')'
    return str1

def postorder(parserTree):
    str1 = ''
    if parserTree:
        str1 = '(' + postorder(parserTree.getLeftChild())
        str1 = str1 + postorder(parserTree.getRightChild())
        str1 = str1 + parserTree.getRootVal() + ')'


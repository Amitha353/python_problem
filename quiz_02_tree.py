import numpy as np


class Tree(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.node = None


def genTree(lst):
    m, n = np.shape(lst)
    tr = Tree()
    tr.node = lst[0][0]
    tr.left = Tree()
    tr.left.node = lst[0][1]
    for a in range(1, m):
        tr = getTheRoot(tr, lst[a][0], lst[a][1])

    print(printTree(tr))
    return tr


def getTheRoot(tre, nod, val):
    if tre.node == nod:
        if tre.left:
            if not tre.right:
                tre.right = Tree()
                tre.right.node = val
        else:
            tre.left = Tree()
            tre.left.node = val
    else:
        if tre.left:
            getTheRoot(tre.left, nod, val)
        if tre.right:
            getTheRoot(tre.right, nod, val)
    return tre


def printTree(tre):
    par = "("
    par += str(tre.node)
    if tre.left:
        par += printTree(tre.left)
    if tre.right:
        par += printTree(tre.right)
    par += ")"
    return par


def testTree(lst, tree):
    m, n = np.shape(lst)
    for a in range(1, m):
        if not checkInTree(tree, lst[a][0]):
            print(lst[a][0], "Not a Tree")
        if not checkInTree(tree, lst[a][1]):
            print(lst[a][1], "Not a Tree")


def checkInTree(tre, nod):
    ck = False
    lck = False
    rck = False
    if tre.node == nod:
        ck = True
    if tre.left:
        lck = checkInTree(tre.left, nod)
    if tre.right:
        rck = checkInTree(tre.right, nod)
    return ck ^ (lck or rck)


lst = (('A', 'B'), ('A', 'C'), ('B', 'G'),
       ('C', 'H'), ('E', 'F'), ('B', 'D'), ('C', 'E'))
lst = (('A', 'B'), ('B', 'D'), ('D', 'E'), ('E', 'G'), ('A', 'C'), ('C', 'F'))
tree = genTree(lst)
testTree(lst, tree)

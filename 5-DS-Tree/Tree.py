"""
TIP: This is how to import a python module from different path by adding path in sys dynamically
"""
import sys
sys.path.insert(0, '../Misc')
import Bit_Manipulation

from queue import Queue

sys.path.insert(0, '../3-Stack-Queue')
from STACK import Stack


class TreeNode:
    def __init__(self, val, left=None, right=None, nextRight=None):
        self.val = val
        self.left = left
        self.right = right
        self.nextRight = nextRight

class DLLNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class TreeModificationSolution():

    def BSTToDLL(self, root):
        def BSTtoDLLRecur(root):
            # Base case
            if root is None:
                return None

            # Traversal: LCR = InOrder
            prev = BSTtoDLLRecur(root.left)

            # Current Node
            cur = DLLNode(root.val)
            cur.prev = prev
            if prev is not None:
                prev.next = cur

            cur.next = BSTtoDLLRecur(root.right)
            return cur

        head = BSTtoDLLRecur(root)
        return head

    def flatten(self, root):
        def flattenRecur(root):
            # Base case
            if root is None:
                return None

            # Traversal: LCR = InOrder
            prev = flattenRecur(root.left)

            # Current Node
            cur = root
            cur.left = prev
            if prev is not None:
                prev.right = cur

            cur.right = flattenRecur(root.right)
            return cur

        newRoot = flattenRecur(root)
        return newRoot

    # def BSTtoDLLRecur_old(self, root):
    #
    #     if root is None:
    #         return
    #
    #     # Traversal: LCR to form a linkedList
    #     self.BSTtoDLLRecur(root.left)
    #
    #     if not self.prev:
    #         self.head = root
    #     else:
    #         root.left = self.prev
    #         self.prev.right = root
    #
    #     self.prev = root
    #     self.BSTtoDLLRecur(root.right)

class Iterator(TreeNode):

    def __init__(self, root):
        self.root = root
        TreeNode.__init__(self, root.val, root.left, root.right, root.nextRight)

    def leftMost(self, root):
        if root is None:
            return None
        while root.left is not None:
            root = root.left
        return root

    def inOrderSuccessor(self, node):
        root = self.root
        if root is None or node is None:
            return None
        """
        From InOrder (LCR) Visit, 3 possible conditions for successor
        1. Successor(C) --> If C has R subtree then leftmost of R is successor
        2. Successor(L) --> If root.left = L,  then root(C) is successor
        3. Successor(R) --> If root.right = R, then root's, parent from where diverge left is successor
        """
        # 1)
        if node.right is not None:
            suc = self.leftMost(node.right)

        # 2) & 3) Search for node's val in BST
        while root is not None:
            if node.val < root.val:
                # <----- Successor(L)
                suc = root
                root = root.left
            elif node.val > root.val:
                # ------> Successor(R)
                root = root.right
            else:
                # Match
                break

        return suc


"""
TREE TRAVERSALS:
"""

class TreeFunction(object):

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.inorderRecur(root, res)
        return res

    def inorderRecur(self, root, res):
        if root is None:
            return

        self.inorderRecur(root.left, res)
        res.append(root.val)
        self.inorderRecur(root.right, res)


def PreOrderTraversal(root):
    if root is None:
        return
    print((root.val,))
    PreOrderTraversal(root.left)
    PreOrderTraversal(root.right)


def InOrderTraversal(root):
    if root is None:
        return
    InOrderTraversal(root.left)
    print((root.val,))
    InOrderTraversal(root.right)


def PostOrderTraversal(root):
    if root is None:
        return
    PostOrderTraversal(root.left)
    PostOrderTraversal(root.right)
    print((root.val,))

"""Iterative Inorder
LeetCode Submisison: https://leetcode.com/problems/binary-tree-inorder-traversal/
https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion/
"""
def iterativeInorder(root):
    s = Stack()
    current = root

    # Base case: Go until NULL nodes or stack is empty
    while current != None or not s.isEmpty():
        while current != None:
            s.push(current)
            current = current.left

        # L node: Pop and visit
        current = s.peek()
        s.pop()
        print(current.val, end=' ')

        """
        We have visited node and node's left
        now it's right subtree
        """
        current = current.right

"""
TREE TRAVERSALS:
Level order
"""
def TreeBFS(root):
    q = Queue()
    q.put(root)
    while not q.empty():
        node = q.get()
        print(node.val, end=' ')

        if node.left:
            q.put(node.left)
        if node.right:
            q.put(node.right)
    print("All Tree Nodes visited")


"""
TREE CREATE/UPDATE/DELETE
BST from list
"""
def createBSTFromInOrderListUtil(mylist, low, high):
    if low <= high:
        middle = (low + high) // 2
        node = TreeNode(mylist[middle], None, None)
        print("Creating Node ", node.val)
        node.left = createBSTFromInOrderListUtil(mylist, low, middle - 1)
        node.right = createBSTFromInOrderListUtil(mylist, middle + 1, high)
        return node


def createBSTFromInOrderList(myList):
    return createBSTFromInOrderListUtil(myList, 0, len(myList)-1)


def insertNode(node, val):
    if node is None:
        # Make root
        node = TreeNode(val)
    elif val <= node.val:
        node.left = insertNode(node.left, val)
    else:
        node.right = insertNode(node.right, val)
    return node

def findLeftMost(root):
    current = root
    while current is not None:
        current = current.left
    return current

"""
Binary Search Tree | Set 2 (Delete)
https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/
"""
def deleteNode(root, valToBeDeleted):
    # Base case: root is None then its over
    if root is None:
        return root

    if valToBeDeleted < root.val:
        # val is less, so Go left, delete from L subtree
        root.left = deleteNode(root.left, valToBeDeleted)
    elif valToBeDeleted > root.val:
        root.right = deleteNode(root.right, valToBeDeleted)
    else:
        # val MAtch: This node is TO BE DELETED
        # 1)
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        else:
            # 3) Node with 2 children
            temp = findLeftMost(root.right)
            root.val = temp.val
            # delete the inorder successor
            root.right = deleteNode(root, temp.val)
    return root

def deleteNode_Original(node, val):
    if node is None:
        return node
    elif val < node.val:
        node.left = deleteNode(node.left, val)
    elif val > node.val:
        node.right = deleteNode(node.right, val)
    else:
        # Whoohoo we FOUND the node to be deleted
        # prepare to be deleted
        if node.right is None and node.left is None:
            """Case 1: No child"""
            del node
        elif node.left is None:
            """Case 2: 1 child"""
            tmp = node.right
            node = node.right
            del tmp
        elif node.right is None:
            tmp = node.left
            node = node.left
            del tmp
        else:
            """Case 3: 2 children"""
            tmp = findMin(node.right)
            node.val = tmp.val
            node.right = deleteNode(node.right, tmp.val)
    return node

def searchInBST(root, val):
    # Empty tree
    if root is None:
        return 0

    # Match found
    if val == root.val:
        return root

    if val > root.val:
        # Search in right subtree
        return searchInBST(root.right, val)
    else:
        # Search in left subtree
        return searchInBST(root.left, val)


def createBST(mylist):
    root = None
    for ele in mylist:
        print("Creating node: {0}".format(ele))
        root = insertNode(root, ele)
    return root


def createBinaryTreeFromList_Helper(mylist, start, end):
    if start > end:
        return None

    # Constraint for the Node
    mid = (start + end) >> 1
    root = TreeNode(mylist[mid])

    # Same Constraint for L & R
    root.left = createBinaryTreeFromList_Helper(mylist, start, mid - 1)
    root.right = createBinaryTreeFromList_Helper(mylist, mid + 1, end)
    return root


def createBinaryTreeFromList(mylist):
    if mylist is []:
        return None

    start, end = 0, len(mylist)-1
    return createBinaryTreeFromList_Helper(mylist, start, end)


def countBitsInTree(root):
    total = 0
    if root is None:
        return 0

    # InOrder Traversal

    # Constraint for root = Count Bits for root node
    total += Bit_Manipulation.TreeFunction.countBits(root.val)

    # Same Constraint for L & R Subtrees = Count Bits for L & R Subtrees
    total += countBitsInTree(root.left)
    total += countBitsInTree(root.right)
    return total




"""
TREE ALGORITHMS
Step 1: identify Traversal that fits
Step 2: Base case
Step 3: Constraint for root
Step 4: Constraint for L & R subtree (most likely similar constraint as root)
"""
def minDepth(root):
    if root is None:
        return 0
    return 1 + min(minDepth(root.left), minDepth(root.right))


def maxDepth(root):
    if root is None:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))


mylist = [i for i in range(1, 11)]
root = createBST(mylist)
TreeBFS(root)
s = TreeModificationSolution()
head = s.BSTToDLL(root)
cur = head

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right = TreeNode(5)
root.right.right = TreeNode(6)
TreeBFS(root)
newRoot = s.flatten(root)
TreeBFS(newRoot)

""" Example BST """
# myList = [10, 11, 2, 7, 15, 17, 5]
# myInOrderList = [2, 5, 7, 10, 11, 15, 17]
# myPreOrderList = [10, 5, 2, 7, 15, 11, 17]
# myPostOrderList = [2, 7, 5, 11, 17, 15, 10]
#
# myInOrderList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# root = createBinaryTreeFromList(myInOrderList)
#
# s = TreeFunction()
# print("inorder traversal....")
# print(s.inorderTraversal(root))
#
# print "InOrder Recursive Traversal:"
# InOrderTraversal(root)
# print "InOrder Iterative Traversal"
# iterativeInorder(root)

"""
From InOrder (LCR) Visit, 3 possible conditions for successor
1. Successor(C) --> If C has R subtree then leftmost of R is successor
2. Successor(L) --> If root.left = L,  then root(C) is successor
3. Successor(R) --> If root.right = R, then root's, parent from where diverge left is successor
"""
# node = root.right
# iter = Iterator(root)
# suc = iter.inOrderSuccessor(node)
# print "\ninOrderSuccessor of {} is {}".format(node.val, suc.val)

"""
node = root.right
suc = inOrderSuccessor(root, node)
print "\ninOrderSuccessor of {} is {}".format(node.val, suc.val)

node = root.right.left
suc = inOrderSuccessor(root, node)
print "\ninOrderSuccessor of {} is {}".format(node.val, suc.val)

node = root.left.right
suc = inOrderSuccessor(root, node)
print "\ninOrderSuccessor of {} is {}".format(node.val, suc.val)
"""

# print "Total Bits 1s in Tree is = {}".format(countBitsInTree(root))
# print "Max Depth = {}, Min Depth = {}".format(maxDepth(root), minDepth(root))


# root = createBSTFromInOrderList(myInOrderList, 0, len(myInOrderList)-1)
# root = createBST(myPreOrderList)
# root = createBST(myPostOrderList)

# InOrderTraversal(root)
# PreOrderTraversal(root)
# PostOrderTraversal(root)
#
# mylist = [10, 5, 15, 1, 6, 12, 20, 3, 30]
# mylist = [i for i in range(1, 11)]
# root = createBST(mylist)
# #PreOrderTraversal(root)
# #InOrderTraversal(root)
# #PostOrderTraversal(root)
# TreeBFS(root)
# s = TreeModificationSolution()
# head = s.BSTtoDLL(root)
# TreeBFS(head)

# deleteNode(root, 30)
# deleteNode(root, 1)
# TreeBFS(root)



"""
root = createBST(mylist)
PreOrderTraversal(root)
InOrderTraversal(root)
PostOrderTraversal(root)
TreeBFS(root)
"""
"""
searchNode = searchInBST(root, 10)
if searchNode:
    print "Found {0}: {1}".format(searchNode.val, "True")
else:
    print "Not Found"

print "Deleting node: {0}".format(10)
deleteNode(root, 10)

searchNode = searchInBST(root, 10)
if searchNode:
    print "Found {0}: {1}".format(searchNode.val, "True")
else:
    print "Not Found"
"""
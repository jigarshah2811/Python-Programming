from queue import Queue
from .LL import DLLNode


class TreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def TreeToDLL(root, HeadRef):
    # Base case
    if root is None:
        return HeadRef

    # Reverse InOrder traversal
    HeadRef = TreeToDLL(root.right, HeadRef)

    # Create a new LL node and attach to HeadRef
    newNode = DLLNode(root.data)
    newNode.next = HeadRef
    if HeadRef is not None:
        HeadRef.prev = newNode
    HeadRef = newNode

    HeadRef = TreeToDLL(root.left, HeadRef)
    return HeadRef


def printLL(head):
    current = head

    print("Printing original:")
    while current.__next__ is not None:
        print(current.item, end=' ')
        current = current.__next__
    print(current.item)

    # Print in reverse
    print("Printing reverse:")
    while current.prev is not None:
        print(current.item, end=' ')
        current = current.prev
    print(current.item)


def FindLCA(root, A, B):
    # Base case
    if root is None:
        return

    # 1) Constraint for the node
    if root.data == A or root.data == B:
        return root

    # 2) Constraint for L & R
    l_lca = FindLCA(root.left, A, B)
    r_lca = FindLCA(root.right, A, B)

    # If both nodes found in Left & Right subtree, root is LCA
    if l_lca and r_lca:
        return root

    # If both nodes not found, then no LCA exists
    if l_lca is None and r_lca is None:
        return None

    # If both nodes found on L, L is LCA else right
    return l_lca if l_lca is not None else r_lca


def LeftTreeView(root):
    q = Queue()
    q.put(root)

    while not q.empty():
        n = q.qsize()
        queueSize = n

        while n > 0:
            node = q.get()

            # If this is the first node in this Level
            if n == queueSize:
                print(node.data, end=' ')
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
            n -= 1
    return


def RightTreeView(root):
    q = Queue()
    q.put(root)

    while not q.empty():
        n = q.qsize()
        queueSize = 1

        while n > 0:
            node = q.get()

            # If this is the first node in this Level
            if n == queueSize:
                print(node.data, end=' ')
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
            n -= 1
    return

"""
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(9)

print FindLCA(root, 4, 5).data
print FindLCA(root, 5, 6).data
print FindLCA(root, 2, 4).data
retNode = FindLCA(root, 9, 8)
if retNode is not None:
    print retNode.data
else:
    print "Node doesn't exist"


# LeftTreeView(root)
# RightTreeView(root)
"""

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(9)
root.left.left = TreeNode(2)
root.left.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(10)
root.right.right.right = TreeNode(20)

head = TreeToDLL(root, None)
printLL(head)





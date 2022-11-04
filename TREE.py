import Queue


class TreeNode:
    def __init__(self, key, left=0, right=0):
        self.key = key
        self.left = left
        self.right = right


def PreOrderTraversal(root):
    if root is None:
        return
    print root.key,
    PreOrderTraversal(root.left)
    PreOrderTraversal(root.right)


def InOrderTraversal(root):
    if root is None:
        return
    InOrderTraversal(root.left)
    print root.key,
    InOrderTraversal(root.right)


def PostOrderTraversal(root):
    if root is None:
        return
    PostOrderTraversal(root.left)
    PostOrderTraversal(root.right)
    print root.key,


def TreeBFS(root):
    q = Queue.Queue()
    q.put(root)
    while not q.empty():
        node = q.get()
        print node.key,

        if node.left:
            q.put(node.left)
        if node.right:
            q.put(node.right)
    print "All Tree Nodes visited"


def createBSTFromInOrderList(mylist, low, high):
    if low <= high:
        middle = (low + high) // 2
        node = TreeNode(mylist[middle], None, None)
        node.left = createBSTFromInOrderList(mylist, low, middle-1)
        node.right = createBSTFromInOrderList(mylist, middle+1, high)
        return node


def insertNode(node, val):
    if node is None:
        # Make root
        node = TreeNode(val, None, None)
    elif val <= node.key:
        node.left = insertNode(node.left, val)
    else:
        node.right = insertNode(node.right, val)
    return node


def findMin(root):
    while root.left:
        root = root.left
    return root


def deleteNode(node, val):
    if node is None:
        return node
    elif val < node.key:
        node.left = deleteNode(node.left, val)
    elif val > node.key:
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
            node.key = tmp.key
            node.right = deleteNode(node.right, tmp.key)
    return node


def searchInBST(root, val):
    # Empty tree
    if root is None:
        return 0

    # Match found
    if val == root.key:
        return root

    if val > root.key:
        # Search in right subtree
        return searchInBST(root.right, val)
    else:
        # Search in left subtree
        return searchInBST(root.left, val)


def createBST(mylist):
    root = None
    for ele in mylist:
        print "Creating node: {0}".format(ele)
        root = insertNode(root, ele)
    return root


""" Example BST """
myList = [10, 11, 2, 7, 15, 17, 5]
myInOrderList = [2, 5, 7, 10, 11, 15, 17]
myPreOrderList = [10, 5, 2, 7, 15, 11, 17]
myPostOrderList = [2, 7, 5, 11, 17, 15, 10]

# root = createBSTFromInOrderList(myInOrderList, 0, len(myInOrderList)-1)
# root = createBST(myPreOrderList)
# root = createBST(myPostOrderList)

# InOrderTraversal(root)
# PreOrderTraversal(root)
# PostOrderTraversal(root)

"""
root = createBST(mylist, 0, len(mylist)-1)
PreOrderTraversal(root)
InOrderTraversal(root)
PostOrderTraversal(root)
TreeBFS(root)
"""

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
    print "Found {0}: {1}".format(searchNode.key, "True")
else:
    print "Not Found"

print "Deleting node: {0}".format(10)
deleteNode(root, 10)

searchNode = searchInBST(root, 10)
if searchNode:
    print "Found {0}: {1}".format(searchNode.key, "True")
else:
    print "Not Found"
"""
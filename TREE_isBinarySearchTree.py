from TREE import createBST


def isBSTUtil(root, min, max):
    if root is None:
        # Empty root is binary root
        return True

    if root.key < min or root.key > max:
        return False

    leftBST = isBSTUtil(root.left, min, root.key)
    rightBST = isBSTUtil(root.right, root.key, max)
    return leftBST and rightBST


def isBinarySearchTree(root):
    return isBSTUtil(root, 0, 50000)


# build a tree
numlist = [1, 2, 3, 4, 5, 6, 7]
root = createBST(numlist, 0, len(numlist) - 1)
res = isBinarySearchTree(root)
print(res)

# build a tree
numlist = [3, 2, 1, 4, 5, 6, 7]
root = createBST(numlist, 0, len(numlist) - 1)
res = isBinarySearchTree(root)
print(res)

# build a tree
numlist = [1, 2, 3, 4, 5, 7, 6, 8]
root = createBST(numlist, 0, len(numlist) - 1)
res = isBinarySearchTree(root)
print(res)

numlist = [1, 2, 5, 10, 12, 15, 20]
root = createBST(numlist, 0, len(numlist) - 1)
res = isBinarySearchTree(root)
print(res)

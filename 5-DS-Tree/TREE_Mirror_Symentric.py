from .Tree import TreeNode, InOrderTraversal

# TODO: BUG: Either in Mirror or isMirror


def isMirror(src, dest):
    # Empty trees are mirror
    if (src is None) and (dest is None):
        return True
    # On of them is Empty! Can't be mirror
    if (src is None) or (dest is None):
        return False
    """
    MIRROR TREE should follow these rules
    // 1 - Their root TreeNode's key must be same
    // 2 - left subtree of left tree and right subtree
    //      of right tree have to be mirror images
    // 3 - right subtree of left tree and left subtree
    //      of right tree have to be mirror images
    """
    return src.key == dest.key and isMirror(src.left, dest.right) and isMirror(src.right, dest.left)


def isSymentricTree(root):
    return isMirror(root, root)


def swap(left, right):
    return right, left


def Mirror(root):
    if root is None:
        return
    root.left, root.right = swap(root.left, root.right)
    Mirror(root.left)
    Mirror(root.right)
    return root


# build a mirror tree
numlist = [1, 2, 3, 4, 6]
tree1 = TreeNode(1, None, None)
tree1.left = TreeNode(2, None, None)
tree1.right = TreeNode(3, None, None)
tree1.left.left = TreeNode(4, None, None)
tree1.right.left = TreeNode(6, None, None)

print("Before Mirror: ")
InOrderTraversal(tree1)

print("After Mirror: ")
tree2 = Mirror(tree1)
InOrderTraversal(tree2)

print("Is Mirror: ")
res = isMirror(tree1, tree2)
print("Is Mirror Tree: {0}".format(res))

res = isSymentricTree(tree1)
print("Is Symentric Tree: {0}".format(res))

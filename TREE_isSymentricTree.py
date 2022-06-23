from TREE import TreeNode, InOrderTraversal


def isMirror(src, dest):
    # Empty trees are mirror
    if (src is None) and (dest is None):
        return True

    """
    MIRROR TREE should follow these rules
    // 1 - Their root TreeNode's key must be same
    // 2 - left subtree of left tree and right subtree
    //      of right tree have to be mirror images
    // 3 - right subtree of left tree and left subtree
    //      of right tree have to be mirror images
    """
    if (src is None) or (dest is None) or (src.key != dest.key):
        return False
    return isMirror(src.left, dest.right) and isMirror(src.right, dest.left)


def isSymentricTree(root):
    return isMirror(root, root)


def swap(left, right):
    return right, left


def Mirror(root):
    if root is None:
        return
    Mirror(root.left)
    Mirror(root.right)
    root.right, root.left = swap(root.left, root.right)
    return root


# build a tree
numlist = [1, 2, 3, 4, 5, 6, 7]
root = TreeNode(1, None, None)
root.left = TreeNode(2, None, None)
root.right = TreeNode(2, None, None)
root.left.left = TreeNode(4, None, None)
root.left.right = TreeNode(3, None, None)
root.right.left = TreeNode(3, None, None)
root.right.right = TreeNode(4, None, None)

InOrderTraversal(root)
root = Mirror(root)
print "After Mirror"
InOrderTraversal(root)

res = isSymentricTree(root)
print "Is Symentric Tree: {0}".format(res)

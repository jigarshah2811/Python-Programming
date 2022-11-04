"""
http://www.geeksforgeeks.org/find-count-of-singly-subtrees/
"""
from .Tree import TreeNode
count = 0


def count_singly(root):
    global count
    count_singly_util(root)
    return count


def isLeaf(root):
    if root.left is None and root.right is None:
        return True


def count_singly_util(root):
    global count
    # Base case
    if root is None:
        return False

    if isLeaf(root):
        count += 1
        return True

    l = count_singly_util(root.left)
    r = count_singly_util(root.right)

    if l and root.key != root.left.key:
        return False
    if r and root.key != root.right.key:
        return False

    count += 1
    return True


# Driver program to test
"""Let us contruct the below tree
            5
          /   \
        4       5
       /  \      \
      4    4      5
"""
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(4)
root.left.right = TreeNode(4)
root.right.right = TreeNode(5)
print("Count of Single Valued Subtress is", count_singly(root))

# Python program to find the count of single valued subtrees

from .TREE_Unival import count_singly

# Node Structure
class Node:
    # Utility function to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# This function increments count by number of single
# valued subtrees under root. It returns true if subtree
# under root is Singly, else false.
def countSingleRec(root, count):
    # Return False to indicate None
    if root is None:
        return True

    # Recursively count in left and right subtress also
    left = countSingleRec(root.left, count)
    right = countSingleRec(root.right, count)

    # If any of the subtress is not singly, then this
    # cannot be singly
    if left == False or right == False:
        return False

    # If left subtree is singly and non-empty , but key
    # doesn't match
    if root.left and root.key != root.left.key:
        return False

    # same for right subtree
    if root.right and root.key != root.right.key:
        return False

    # If none of the above conditions is True, then
    # tree rooted under root is single valued,increment
    # count and return true
    count[0] += 1
    return True


# This function mainly calss countSingleRec()
# after initializing count as 0
def countSingle(root):
    # initialize result
    count = [0]

    # Recursive function to count
    countSingleRec(root, count)

    return count[0]



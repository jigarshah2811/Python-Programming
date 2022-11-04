from .Tree import TreeNode, InOrderTraversal, createBinaryTreeFromList, PreOrderTraversal


"""
http://www.geeksforgeeks.org/connect-nodes-at-same-level/
Initially, all the nextRight pointers point to garbage values. Your function should set these pointers to point next right for each node.

Example

Input Tree
       A
      / \
     B   C
    / \   \
   D   E   F


Output Tree
       A--->NULL
      / \
     B-->C-->NULL
    / \   \
   D-->E-->F-->NULL
"""


def connectHelper(root):
    if root is None:
        return

    # PreOrder Traversal CLR
    # 1) Constraint for root
    if root.left:
        root.left.nextRight = root.right
    if root.right:
        root.right.nextRight = root.nextRight.left if root.nextRight is not None else None

    # 2) Constraint for L & R Subtree
    connectHelper(root.left)
    connectHelper(root.right)
    return root


def connect(root):
    if root is None:
        return None
    root.nextRight = None
    return connectHelper(root)


def isMirror(src, dest):
    # Validations
    if src is None and dest is None:
        # Empty tree are Mirror Tree
        return True

    if src is None or dest is None:
        # One is empty, can't be Mirror Tree
        return False

    """
    MIRROR TREE should follow these rules
    // 1 - Their root TreeNode's key must be same
    // 2 - left subtree of left tree and right subtree
    //      of right tree have to be mirror images
    // 3 - right subtree of left tree and left subtree
    //      of right tree have to be mirror images
    """
    # 1) Constraint for the node
    if src.key != dest.key:
        return False

    # 2) Same constraint for L & R Subtrees
    l = isMirror(src.left, dest.right)
    r = isMirror(src.right, dest.left)
    return l & r


"""
         root
      /       \
    a     |     a
   / \    |    / \
  b   c   |   c   b
 / \      |      / \
d   e     |      e  d    return true

         root
      /       \
    a     |     a
   / \    |    / \
  b   c   |   c   c
 / \      |      / \
d   e     |      e  d    return false

struct Node {
  int data;
  Node *left;
  Node *right; 
} Node;

bool isSelfMirror(root) {
  return true or false;
}
"""


def isMirror(src, dest):
    # Validations
    # If both are none, return True
    if src is None and dest is None:
        return True

    if src is None or dest is None:
        return False

    # 1) Root matches
    # 2) Constraint for L & R Subtree matches
    return src.data == dest.data and isMirror(src.left, dest.right) and isMirror(src.right, dest.left)


def isSelfMirror(root):
    # Empty tree is mirro
    if root is None:
        return True
    return isMirror(root.right, root.left)


def isSymentricTree(root):
    return isMirror(root, root)


def isLeaf(root):
    if root.left is None and root.right is None:
        return True
    return False

"""
TESTCASES for all TREE Functions here!
"""


def main():
    inOrderList = [1, 2, 3, 4, 5, 6, 7]
    root = createBinaryTreeFromList(inOrderList)
    InOrderTraversal(root)
    mirror = Mirror(root)
    print("\nAfter Mirror")
    InOrderTraversal(mirror)

    inOrderList = [1, 2, 3, 4, 5, 6, 7]
    root = createBinaryTreeFromList(inOrderList)
    print("\nIsMirror: {}".format(isMirror(root, mirror)))

    inOrderList = [1, 2, 3, 4, 5, 6, 8]
    root = createBinaryTreeFromList(inOrderList)
    print("\nIsMirror: {}".format(isMirror(root, mirror)))

    inOrderList = [9, 3, 7, 5, 7, 3, 9]
    SymantricTree = createBinaryTreeFromList(inOrderList)
    res = isSymentricTree(SymantricTree)
    print("\nIs Symentric Tree: {0}".format(res))

    inOrderList = [9, 3, 7, 5, 8, 3, 9]
    SymantricTree = createBinaryTreeFromList(inOrderList)
    res = isSymentricTree(SymantricTree)
    print("\nIs Symentric Tree: {0}".format(res))

    inOrderList = [1, 2, 3, 4, 5, 6, 7]
    root = createBinaryTreeFromList(inOrderList)
    connectedTree = connect(root)
    print("\nConnected TREE: {}".format(connectedTree))


if __name__ == "__main__":
    main()

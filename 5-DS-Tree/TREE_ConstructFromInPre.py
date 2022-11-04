from .Tree import TreeNode, InOrderTraversal
"""
https://www.geeksforgeeks.org/?p=17138
Sorted Array to Balanced BST
"""

def search(arr, start, end, value):
    for i in range(start, end+1):
        if arr[i] == value:
            return i


"""Recursive function to construct binary of size len from
   Inorder traversal in[] and Preorder traversal pre[].  Initial values
   of inStrt and inEnd should be 0 and len -1.  The function doesn't
   do any error checking for cases where inorder and preorder
   do not form a tree """
def buildTreeFromInOrderPreOrder(preOrder, inOrder, inLow, inHigh):
    # Base Case: If indexes cross, no more nodes to be created
    if inLow > inHigh:
        return None

    # 1) Constraint for root: Find preIndex node from InOrder List and create that as root
    inIndex = inOrder.index(preOrder[buildTreeFromInOrderPreOrder.preIndex])
    buildTreeFromInOrderPreOrder.preIndex += 1
    root = TreeNode(inOrder[inIndex])
    print("Creating node: {0}".format(inOrder[inIndex]))

    # Base case: If this is leaf node from preOrder seq, no children for L & R
    if inLow == inHigh:
        return root

    # 2) Same constraint for L & R subtree: LeftArray becomes L subtree, RightArray becomes R subtree
    root.left = buildTreeFromInOrderPreOrder(preOrder, inOrder, inLow, inIndex-1)
    root.right = buildTreeFromInOrderPreOrder(preOrder, inOrder, inIndex+1, inHigh)

    return root


def sortedArrayToBST(A, low, high):
    # Base Case, when to return
    if high - low < 0:
        return None

    # Constraint for root, Create middle node
    mid = (low + high) / 2 # (low + high) >> 1
    root = TreeNode(A[mid])
    print("Creating Node: {0}".format(root.key))

    # Same constraint for L & R Subtree
    # Left is Left Half of Array, Right is Right half of Array
    root.left = sortedArrayToBST(A, low, mid-1)
    root.right = sortedArrayToBST(A, mid + 1, high)
    return root


"""
Boundary traversal of a BT
https://www.geeksforgeeks.org/?p=23796
"""
def printLeafNodes(root):
    if root:
        printLeafNodes(root.left)
        if root.left is None and root.right is None:
            print(root.key)
        printLeafNodes(root.right)
def printLeftBoundary_TopDown(root):
    # TopDown: First print the node then recurse
    if root:
        if root.left:
            print(root.key)
            printLeftBoundary_TopDown(root.left)

        elif root.right:
            print(root.key)
            printLeftBoundary_TopDown(root.right)


def printRightboundary_BottomUp(root):
    # BottomUp: First recurse then print
    if root:
        if root.left:
            printRightboundary_BottomUp(root.left)
            print(root.key)
        if root.right:
            printRightboundary_BottomUp(root.right)
            print(root.key)

def boundaryTraversal(root):
    if root:
        print(root.key)
        printLeftBoundary_TopDown(root.left)

        printLeafNodes(root.left)
        printLeafNodes(root.right)

        printRightboundary_BottomUp(root.right)


def main():

    # Driver program to test above function
    inOrder = [1, 2, 3, 4, 5, 6, 7, 8]
    preOrder = [5, 2, 1, 3, 4, 7, 6, 8]
    # Static variable preIndex
    buildTreeFromInOrderPreOrder.preIndex = 0
    root = buildTreeFromInOrderPreOrder(preOrder, inOrder, 0, len(inOrder) - 1)

    # Let us test the build tree by priting Inorder traversal
    print("Inorder traversal of the constructed tree is")
    InOrderTraversal(root)

    """
    print "\nSorted Array to Balanced BST"
    root =  sortedArrayToBST(inOrder, 0, len(inOrder)-1)
    InOrderTraversal(root)

    print "Printing outer most bounary traversal for BT"
    print boundaryTraversal(root)
    """



if __name__ == "__main__":
    main()

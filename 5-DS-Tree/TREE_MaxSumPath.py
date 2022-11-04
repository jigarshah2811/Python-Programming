from .Tree import TreeNode, createBSTFromInOrderList, InOrderTraversal

global_sum = 0
target_leaf = TreeNode(0, None, None)


def isLeaf(root):
    if root.left is None and root.right is None:
        return True
    else:
        return False


def maxSumPathHelper(root, currentSum, maxSum, targetLeaf):
    # base case
    if root is None:
        return

    # 1) Constraint for root
    currentSum += root.key

    # Hisab: Is this the leaf with currentSum>MaxSum?
    if isLeaf(root):
        print("Found Leaf: {0} with currentSum={1}".format(root.key, currentSum))
        if  currentSum > maxSum:
            maxSum = currentSum
            targetLeaf = root
        return targetLeaf

    # 2) Constraint for L & R
    # Simply pass root.val to L and R subTree to be added in leaf value

    maxSumPathHelper(root.left, currentSum + root.key, maxSum, targetLeaf)
    maxSumPathHelper(root.left, currentSum + root.key, maxSum, targetLeaf)


def PrintPath(root):
    global target_leaf
    # Base case
    if root is None:
        return False

    if root == target_leaf or PrintPath(root.left) or PrintPath(root.right):
        print(root.key, end=' ')
        return True

    return False


def MaxSumPath(root):
    targetLeaf = None
    currentSum = 0
    maxSum = 0
    return maxSumPathHelper(root, currentSum, maxSum, targetLeaf)



def main():
    myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    root = createBSTFromInOrderList(myList)
    InOrderTraversal(root)

    targetLeaf = MaxSumPath(root)
    print(targetLeaf)
    PrintPath(targetLeaf)



if __name__ == '__main__':
    main()


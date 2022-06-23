from .Tree import TreeNode
from .Tree import createBinaryTreeFromList
from queue import Queue


def printExtremeNodes(root):
    q = Queue()
    q.put(root)
    PrintLeftMost = False

    while not q.empty():
        nodeCount = q.qsize()
        n = nodeCount

        while n != 0:
            node = q.get()
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)

            # Print alternatively
            if PrintLeftMost and n == nodeCount-1:
                print(node.key)
            if not PrintLeftMost and n == 0:
                print(node.key)
            n -= 1

        PrintLeftMost = True


def main():
    TreeNodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
    root = createBinaryTreeFromList(TreeNodes)
    printExtremeNodes(root)


if __name__ == "__main__":
    main()

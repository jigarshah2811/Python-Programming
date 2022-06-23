class TreeNode:
    def __init__(self, val, left=None, right=None, nextRight=None):
        self.val = val
        self.left = left
        self.right = right
        self.nextRight = nextRight


class Solution():
    def detectAndCorrect(self, root):
        def correct():
            # If first and last both detected, discard middle
            if first and last:
                first.val, last.val = last.val, first.val
            elif first and middle:
                first.val, middle.val = middle.val, first.val
            # It's already a valid BST

        def detect(root):
            # Traversal: BST inorder traversal will be array in Sorted ORDER

            if root is None:
                return

            detect(root.left)

            # Cur Node, Detect 2 nodes that violates the sorting constraint
            if prev and root.val < prev.val:
                print(("found {0}".format(root.val)))
                # 1) This is the 1st node that violates constraint
                if not first:
                    first = prev
                    middle = root
                else: # 2) This is the 2nd node that violates constraint
                    last = root

            prev = root

            detect(root.right)

        first, middle, last, prev = None, None, None, None
        detect(root)
        correct()
        return root


def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.val, end=' ')
    inorder(root.right)

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(20)

s = Solution()
expectedRoot = s.detectAndCorrect(root)
#print("Incorrect BST: {0}".format(inorder(root)))
#print("Corrected BST: {0}".format(inorder(root)))


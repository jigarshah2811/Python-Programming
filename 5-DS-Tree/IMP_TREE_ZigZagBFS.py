from .Tree import TreeNode
from .Tree import TreeFunction
import sys
import queue


class Solution:
    def zigzagLevelOrder(self, root):
        if root is None:
            return []

        res = []
        q, tmp, level, directionFlag = [root], [], 0, True

        while q:
            n = len(q)
            for i in range(n):
                # Create a tmp list of this level
                node = q.pop(0)             # TRICK: Use list as QUEUE then pop(0), Use list as STACK then pop(last)
                tmp.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # Level done
            res.append(tmp if directionFlag else tmp[::-1])

            # Reset for next level
            tmp = []
            directionFlag = not directionFlag

        return res


    def isValidBST(self, root):
        min, max = 0, sys.maxsize
        return self.isValidBSTRecur(root, min, max)

    def isValidBSTRecur(self, root, min, max):
        # Base case
        if not root:
            return True

        # Traversal: CLR = PreOrder
        #C) BST must have this constrain satisfied
        if root.val < min or root.val > max:
            return False

        #L) & R)

        l = self.isValidBSTRecur(root.left, min, root.val)
        r = self.isValidBSTRecur(root.left, root.val, max)
        return l and r


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

f = TreeFunction()
print(f.inorderTraversal(root))

s = Solution()
print(s.zigzagLevelOrder(root))
print(s.isBST(root))


from TREE import *

import collections
class Solution:
    def TreeCopy(self, oldroot):
        oldQ = collections.deque([oldroot])

        newroot = TreeNode(oldroot.val)
        newQ = collections.deque([newroot])

        while oldQ and newQ:
            oldNode = oldQ.popleft()
            newNode = newQ.popleft()

            if oldNode.left:
                newNode.left = TreeNode(oldNode.left.val)
                oldQ.append(oldNode.left)
                newQ.append(newNode.left)
            if oldNode.right:
                newNode.right = TreeNode(oldNode.right.val)
                oldQ.append(oldNode.right)
                newQ.append(newNode.right)

        return newroot


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(7)
TreeBFS(root)

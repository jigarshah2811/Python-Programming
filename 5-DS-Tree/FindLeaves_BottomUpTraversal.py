"""
Falling Leaves problem - Bottom up traversal
============================================
Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.

Example:
Given binary tree
          1
         / \
        2   3
       / \
      4   5
Returns [4, 5, 3], [2], [1].

https://www.programcreek.com/2014/07/leetcode-find-leaves-of-binary-tree-java/
"""

from .Tree import TreeNode
import collections

class Solution(object):
    def __init__(self):
        self.d = collections.defaultdict(list)

    def findLeaves(self, root):
        # Traversal: Bottom Up to find leaves.... LRC ... PostOrder
        # Base Case
        if root is None:
            return -1

        # Key is to find the right index for node in result list
        l = self.findLeaves(root.left)
        r = self.findLeaves(root.right)

        # Lets say l and r returns 0, that means both nodes under L & R are leaves
        rootLevel = 1 + max(l, r)
        print(("left:{0} right:{1} rootLevel:{2} value:{3}").format(l,r,rootLevel,root.key))
        self.d[rootLevel].append(root.key)

        return rootLevel

    def getLeavesLevel(self):
        return self.d

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

s = Solution()
s.findLeaves(root)
print(s.getLeavesLevel())

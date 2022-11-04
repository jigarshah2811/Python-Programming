# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.prev = None
        
    def flatten(self, root: Optional[TreeNode]) -> None:
        """ TRAVERSAL: Reverse preorder traversal ---> RLC 
        At C: Current's right is the subtree on right
              Current's left is None
              Carry forward current as prev
        """
        
        if root is None:
            return None
        
        # Example traversal of [4, 3, 2]
        self.flatten(root.right)
        self.flatten(root.left)
        
        # At C
        # 2's right would be entire subtree (2->3->4)
        root.right = self.prev  # The entire sub-treen that was flattern before
        # 2's left is nothing
        root.left = None        # Nothing on left as we reach to root
        
        # Carry forward 2's subtree to become the "right" hand of upcoming node [1] in this case
        self.prev = root


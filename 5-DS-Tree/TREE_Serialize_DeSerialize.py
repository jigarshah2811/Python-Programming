"""
You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"

https://leetcode.com/articles/serialize-and-deserialize-binary-tree/

"""
class TreeNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

def serialize(root):
    # Base case
    if root is None:
        str += 'None'

    # Traversal: PreOrder CLR
    str += str(root.key) + ","
    str = serialize(root.left, str)
    str = serialize(root.right, str)

    return str


def deserialize(node_list, index):
    """ a recurisve helper function for deserialization."""
    index += 1
    root = None

    # check base case
    if node_list[index - 1] != 'None':
        root = TreeNode(node_list[index - 1])
        root.left, index = deserialize(node_list, index)
        root.right, index = deserialize(node_list, index)

    return root, index


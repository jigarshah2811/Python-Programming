import collections
from typing import List
"""
Clone LinkedList with Random pointer
"""
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class CloneLinkedList(object):
    def clone(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:  # Empty list
            return None

        """
        Pattern: Using map {oldNode:NewNode}
        1: Create new nodes for new LL, Create map {oldNode: NewNode} entries for corresponding newNodes
        2: Populate val,next,random for NewNode using oldNode's val, next, random using m[oldNode.next]
        """
        m = collections.defaultdict(Node)
        old = head

        # 1: Create new nodes for new LL, Create map {oldNode: NewNode} entries for corresponding newNodes
        while old is not None:
            print("Creating new node for old: ", old.val)
            new = Node(old.val)
            m[old] = new

            old = old.next
        m[old] = None  # Last entry for None to include in new LinkedList

        print("New Nodes created, but val, next, random to be populated now...")
        # print(m)

        # 2: Populate val,next,random for NewNode using oldNode's val, next, random using m[oldNode.next]
        old = head
        while old is not None:
            m[old].val = old.val
            m[old].next = m[old.next]
            m[old].random = m[old.random]

            print("Populated new node val, next, random ", old.val, m[old.next], m[old.random])
            old = old.next

        return m[head]

""" N Arr Tree """


class TreeNode:
    def __init__(self, val: int, children: List[TreeNode]) -> TreeNode:
        self.val = val
        self.children = children

class TreeCloneSolution:
    def __init__(self):
        self.new = collections.defaultdict(TreeNode)

    def cloneTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None

        # Create a newNode and mapping
        newRoot = TreeNode(root.val)
        self.new[root] = newRoot

        for child in root.children:
            newChild = self.cloneTree(child)
            newRoot.children.append(newChild)

        return newRoot


""" Clone Graph """
class GraphNode():
    def __init__(self, val=0, conns=[]):
        self.val = val
        self.conns = conns

class Solution:
    def cloneGraph(self, oldRoot: GraphNode) -> GraphNode:
        """ Pattern: Using Map... New[OldNode] = NewNode
        phase 1: Create new nodes, create mapping new[oldNode] = newNode
        phase 2: Assign links... Traverse through new Graph and create links (conns) using new[conn] = newConn
        """

        new = collections.defaultdict(GraphNode)
        q = collections.deque()
        visited = set()

        # phase 1 for root
        newRoot = GraphNode(oldRoot.val)
        new[oldRoot] = newRoot

        # Phase 1 for creating simmilar mapping for conns
        q.append(oldRoot)
        while q:
            oldNode = q.popleft()
            visited.add(oldNode)

            for oldConn in oldNode.conns:
                new[oldConn] = GraphNode(oldConn.val)
                visited.add(oldConn)
                q.append(oldConn)

                new[oldNode].conns.append(new[oldConn])

        return newRoot





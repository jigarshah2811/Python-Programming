""" https://leetcode.com/problems/clone-graph/submissions/
    https://leetcode.com/problems/clone-binary-tree-with-random-pointer/
    https://leetcode.com/problems/clone-n-ary-tree/
    https://leetcode.com/problems/copy-list-with-random-pointer/

DS: Associative Map   d{OldNode: NewNode}

Pattern: BFS    NewNode neighbors ma add oldNode na associative nodes as neighbors  -->  d[node].neighbors.append(d[conn])
"""
import collections
class Node:
    def __init__(self, val, neighbors=[]) -> None:
        self.val = val
        self.neighbors = neighbors
        return self
        
class Solution:
    def cloneGraph(self, root: 'Node') -> 'Node':
        """ Associative Map """
        d = collections.defaultdict(Node)
        
        # Edge case
        if root is None: return None
        
        # Create new graph: root
        NewRoot = Node(root.val, None)
        d[root] = NewRoot
        
        # BFS on old graph to visit nodes && create new nodes
        q = collections.deque()
        q.append(root)
        
        while q:
            node = q.popleft()
            
            print(f"Visiting: {node.val}, NewNode: {d[node].val}")
            for conn in node.neighbors:
                if conn in d:   # node already exists in new graph
                    d[node].neighbors.append(d[conn])
                else:           # node doesn't exist in new graph
                    newConn = Node(conn.val, None)
                    d[conn] = newConn
                    d[node].neighbors.append(d[conn])
                    
                    # Keep visiting conns
                    q.append(conn)
                print(f"Visited Conn: {conn.val}, ConnNode: {d[conn].val}")
            print(f"Visited: {node.val}")
        
        return NewRoot


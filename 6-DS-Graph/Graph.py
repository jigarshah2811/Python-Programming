from collections import defaultdict
import collections
import heapq

""" GRAPHS
Study: https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/#introDFSnBFS
"""
class Graph(object):
    def __init__(self):
        self.graph = defaultdict(list)
        self.indegree = dict(int)

    # Directed graph
    def add_edge(self, src, dest):
        self.graph[src].append(dest)

    # Un-Directed graph
    def add_edge_undirected(self, src, dest):
        self.graph[src].append(dest)
        self.graph[dest].append(src)

    # Weighted directed graph
    def add_edge_weighted(self, src, dest, weight=1):
        self.graph[src].append((dest, weight))

    # Weighted Undirected graph
    def add_edge_weighted_undirected(self, src, dest, weight=1):
        self.graph[src].append((dest, weight))
        self.graph[dest].append((src, weight))

    # Topological sort
    def add_edge_topological(self, src, dest):
        self.graph[src].append(dest)
        self.indegree[dest] = self.indegree[src] + 1

    """
    DFS for connected graph
    Study: https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
    """
    def dfs_connected_graph(self, root):
        visited = {}
        # Start from 1 Node....
        self.dfs_recur(root, visited)

    """
    DFS for disconnected graph
    Study: https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
    """
    def dfs_disconnected_graph(self):
        visited = {}

        # Start from ALL Node....
        for node in list(self.graph.keys()):
            if node not in visited or not visited[node]:
                self.dfs_recur(node, visited)


    """
    DFS: Recursive function to visit a node and all it's connections
    """
    def dfs_recur(self, node, visited):
        # PreOrder: Mark this node visited BEFORE visiting connections
        visited[node] = True
        print((node,))

        # Children: Recursively visit all children of this node
        for (conn, weight) in self.graph[node]:
            if conn not in visited:
                self.dfs_recur(conn, visited)

        # PostOrder: Mark this node visited AFTER visiting connections
        # TRICK: Helpful in Installing component AFTER installing all dependancies!
        # visited[node] = True

    """
    Detect cycle
    Read: https://www.geeksforgeeks.org/detect-cycle-in-a-graph/
    """
    def is_cycle(self):
        visited = {}
        recordingStack = {}

        # disconnected graph, so start with ALL nodes
        for node in list(self.graph.keys()):
            if node not in visited or not visited[node]:
                if self.is_cycle_recur(node, visited, recordingStack):
                    return True
        return False

    def is_cycle_recur(self, node, visited, recordingStack):
        # Mark current node as visited and
        visited[node] = True

        # START of recording stack: for DFS
        recordingStack[node] = True

        # Visit all connections
        for (conn, weight) in self.graph[node]:
            # IN-BETWEEN: recStack! = Cycle -
            # We are re-visiting this node (conn) from the same dfs stack of original node
            if recordingStack[conn]:
                return True
            elif conn not in visited or visited[conn] == False:
                self.is_cycle_recur(conn, visited, recordingStack)

        # END of recording stack: for DFS
        recordingStack[node] = False
        return False


    """
    Find Path from Src to Dest
    Read: https://www.geeksforgeeks.org/find-if-there-is-a-path-between-two-vertices-in-a-given-graph/
    """
    def find_path(self, src, dest):
        visited = {}
        for node in list(self.graph.keys()):
            if node not in visited:
                if self.find_path_dfs(node, src, dest, visited):
                    return True
        return False

    def find_path_dfs(self, node, src, dest, visited):
        # PreOrder: Mark this node visited
        visited[node] = True

        # Now visit all connections
        for (conn, weight) in self.graph[node]:
            """
            TRICK!!! During DFS if the target node is found from source, exit!!!
            """
            if conn == dest:
                return True

            if conn not in visited or not visited[conn]:
                if self.find_path_dfs(conn, src, dest, visited):
                    return True

        # Everything is visited, but target not found yet
        return False

    """
    BFS for connected Graph
    Study: https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
    """
    def bfs_connected_graph(self, root):
        q = collections.deque()
        visited = set()

        q.append(root)      # Start from root node!

        while q:            # Keep going till there is any left node in Q
            node = q.popleft()     # Visit the 1st node from queue

            # PreOrder: Visit the node BEFORE it's connections
            if node not in visited:
                visited.add(node)
                print((node,))

            # Add all connections of this node in queue to be visited later: Visiting children is deferred!
            for conn in self.graph[node]:
                if conn not in visited:
                    q.append(conn)          # QUEUE UP to visit later!

    """
    BFS for WEIGHTED Dis-connected Graph
    Study: https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
    """
    def bfs_disconnected_graph(self):
        q = collections.deque()
        visited = set()

        for root in self.graph: # Start from ALL ROOT nodes, different from connected graph where there's only 1 root
            q.append(root)

        while q:            # Keep going till there is any left node in Q
            node = q.popleft()     # Visit the 1st node from queue

            # PreOrder: Visit the node BEFORE it's connections
            if node not in visited:
                visited.add(node)
                print((node,))

            # Add all connections of this node in queue to be visited later: Visiting children is deferred!
            for conn in self.graph[node]:
                if conn not in visited:
                    q.append(conn)          # QUEUE UP to visit later!

    def printGraph(self):
        return sorted(list(self.graph.items()), key=lambda x: x[0])


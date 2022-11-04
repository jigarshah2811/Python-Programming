import collections
from typing import List


class DirectedGraph:
    def __init__(self, edges):
        self.graph = collections.defaultdict(list)
        self.buildGraph(edges)

    def buildGraph(self, edges: List[List]):
        for edge in edges:
            src, dest = edge[0], edge[1]
            self.graph[src].append(dest)

    def dfs(self) -> set:
        def dfs_recur(node):
            visitingStack.append(node)

            print("visiting node: {}".format(node))
            for conn in self.graph[node]:
                if conn in visitingStack: # CYCLE, this node is already on stack of being visited! We started from here!
                    print("CYCLE from node: {} to conn: {}, stack: {}".format(node, conn, visitingStack))
                    break
                elif conn not in visited:
                    dfs_recur(conn)

            visitingStack.pop()
            visited.add(node)

        visitingStack = []
        visited = set()
        # Disconnected Graph
        for root in list(self.graph.keys()):
            if root not in visited:
                dfs_recur(root)
        return visited

class DirectedWeightedGraph:
    def __init__(self, edges):
        self.graph = collections.defaultdict(list)
        self.buildGraph(edges)

    def buildGraph(self, edges: List[List]):
        for edge in edges:          # Format [[node, conn, weight], [node, conn, weight]]
            node, conn, weight = edge[0], edge[1], edge[2]
            self.graph[node].append((conn, weight))

    def dfs(self) -> set:
        def dfs_recur(node):
            print("visiting node: {}".format(node))
            visitingStack.append(node)

            for (conn, weight) in self.graph[node]:
                if conn in visitingStack:  # CYCLE, found node on visiting stack, From where we started...
                    print("CYCLE from node: {} to conn: {}, stack: {}".format(node, conn, visitingStack))
                    continue
                elif conn not in visited:
                    print("Visiting conn: {} from node: {} weight: {}".format(conn, node, weight))
                    dfs_recur(conn)

            # All conns of this node is now visited (on stack), so this node is COMPLETELY visited
            visitingStack.pop()
            visited.add(node)

        visitingStack = []      # Record, nodes being visited in a stack to detect CYCLE
        visited = set()         # Record, nodes completely visited AFTER all conns are visited

        # Disconnected Graph
        for root in list(self.graph.keys()):
            if root not in visited:
                dfs_recur(root)
        return visited

    def allPaths(self, src, target) -> float:
        def dfs_recur(node, total):
            print("visiting node: {}".format(node))
            visitingStack.append(node)

            for (conn, weight) in self.graph[node]:
                total += weight
                print("Visiting conn: {} from node: {} weight: {}".format(conn, node, weight))

                if conn == target:          # FOUND
                    print("DEST HIT: Found target from path: {} Total: {}".format(visitingStack, total))
                    self.minTotal = min(self.minTotal, total)

                    total = 0   # Reset total
                    continue    # Continue to try find another path!
                if conn in visitingStack:  # CYCLE, found node on visiting stack, From where we started...
                    print("CYCLE from node: {} to conn: {}, stack: {}".format(node, conn, visitingStack))
                    continue
                elif conn not in visited:
                    dfs_recur(conn, total)

            # All conns of this node is now visited (on stack), so this node is COMPLETELY visited
            visitingStack.pop()
            visited.add(node)

        visitingStack = []      # Record, nodes being visited in a stack to detect CYCLE
        visited = set()         # Record, nodes completely visited AFTER all conns are visited

        # Disconnected Graph
        self.minTotal = float('inf')
        dfs_recur(src, total=0)
        return self.minTotal

""" DIRECTED GRAPH Example """
"""
edges = [[0, 1], [0, 4], [1, 4], [1, 2], [3, 1], [3, 2], [4, 3]]
graph = DirectedGraph(edges)
print(graph.dfs())
"""

""" DIRECTED WEIGHTED GRAPH Example """
edges = [[0, 1, 2], [0, 4, 4], [1, 4, 4], [1, 2, 3], [3, 1, 7], [3, 2, 1], [4, 3, 1]]
graph = DirectedWeightedGraph(edges)
#print(graph.dfs())
src, dest = 0, 1
minTotal = graph.allPaths(src, dest)
print("DFS: Shortest path from {} to {} is: {}".format(src, dest, minTotal))

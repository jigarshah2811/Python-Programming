# Program to print BFS traversal from a given source
# vertex. BFS(int s) traverses vertices reachable
# from s.
from collections import defaultdict

# This class represents a directed graph using adjacency
# list representation
# Graph = dict(list)
# Example --> graph(0) = [1,2,3], graph(1) = [0, 3,5] and so on...
class Graph:
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def __addEdge__(self, u, v):
        self.graph[u].append(v)

    # Function to print a BFS of graph
    def BFS(self, v):
        # Mark already visited nodes to prevent Cycle/Loop in graph
        visited = {}

        # Create a queue for BFS future visit nodes (visit neighbour, store children to visit in future)
        q = []

        # Store children of v to visit in future
        q.append(v)
        # Mark visited
        visited[v] = True

        # Untill all nodes in graph are visited
        while q:
            # Dequeue a vertex from queue and print it
            node = q.pop(0)
            print node,
            # Get all adjacent vertices of the dequeued
            # vertex s. If a adjacent has not been visited,
            # then mark it visited and enqueue it
            for adjNode in self.graph[node]:
                if adjNode not in visited:
                    # Store children of v to visit in future
                    q.append(adjNode)
                    # Mark visited
                    visited[adjNode] = True



g = Graph()
g.__addEdge__(0, 1)
g.__addEdge__(0, 2)
g.__addEdge__(1, 2)
g.__addEdge__(2, 0)
g.__addEdge__(2, 3)
g.__addEdge__(3, 3)
g.BFS(2)
""" SHORTEST PATH: Weighted DAG with Dijkstra in Python using heapq

Watch video: https://www.youtube.com/watch?v=lAXZGERcDf4
solution: https://gist.github.com/hanfang/89d38425699484cd3da80ca086d78129
"""
import collections
import heapq


class Graph:
    def __init__(self):
        # Weighted DAG - {node --> [(cost,neighbour), ...]}
        self.graph = collections.defaultdict(list)

    def add_edge(self, src, dest, weight):
        self.graph[src].append((weight, dest))

    def printGraph(self):
        print(sorted(list(self.graph.items()), key=lambda x:x[0]))

    def buildGraph(self, edges):
        for edge in edges:
            self.add_edge(edge[0], edge[1], edge[2])

    def shortestPath(self, src, dest):
        visited = set()

        # create a priority queue, node = (cost, dest, [path from src to this dest])
        queue = [(0, src, [])]
        while queue:
            heapq.heapify(queue)
            (nodeCost, node, nodePath) = heapq.heappop(queue)     # Pop Node with minCost to visit!
            print("Visiting Node: {} with current cost: {} from path: {}".format(node, nodeCost, nodePath))

            if node in visited:
                continue        # Skip, the node is already visited
            visited.add(node)

            if node == dest:    # BINGO! Found Destination! Return Shortest cost and Path!
                return cost, nodePath+[node]

            # Otherwise keep looking for target node through neighbors
            for (cost, conn) in self.graph[node]:
                if conn not in visited:
                    queue.append((nodeCost + cost, conn, nodePath+[conn]))  # TRICK: Add cost to src to reach this destNode

        # We completely visited all nodes BUT Target not found....
        return float('inf'), []

# def shortestPath(edges, source, target):
#     # create a weighted DAG - {node:[(cost,neighbour), ...]}
#     graph = collections.defaultdict(list)
#     for fromNode, toNode, cost in edges:
#         graph[fromNode].append((cost, toNode))
#
#     # Check the graph is formulated correct
#     print sorted(graph.items(), key=lambda x: x[0])
#     # hash set to store visited nodes
#     visited = set()
#
#     # Algorithm: Based on BFS
#     # create a priority queue, node = (cost, source, [path from src to dest])
#     queue = [(0, source, [])]
#     heapq.heapify(queue)
#
#     # traverse graph with ===== BFS =======
#     while queue:
#         # Get the node with MIN COST, and visit it
#         (cost, node, path) = heapq.heappop(queue)
#
#         if node not in visited:
#             visited.add(node)
#
#             path = path + [node]
#             # hit the target ??
#             if node == target:
#                 return (cost, path)
#
#             # visit neighbours
#             for c, neighbour in graph[node]:
#                 if neighbour not in visited:
#                     heapq.heappush(queue, (cost + c, neighbour, path))
#     return float("inf")

if __name__ == "__main__":

    edges = [
        ("A", "B", 7),
        ("A", "D", 5),
        ("B", "C", 8),
        ("B", "D", 9),
        ("B", "E", 7),
        ("C", "E", 5),
        ("D", "E", 15),
        ("D", "F", 6),
        ("E", "F", 8),
        ("E", "G", 9),
        ("F", "G", 11)
    ]

    g = Graph()
    g.buildGraph(edges)
    g.printGraph()
    print ("Find the shortest path with Dijkstra")
    print ("A -> E:")
    print((g.shortestPath("A", "E")))

    edges = [
        ("A", "B", 7),
        ("A", "D", 5),
        ("B", "C", 1),
        ("B", "D", 9),
        ("B", "E", 7),
        ("C", "E", 4),
        ("D", "E", 15),
        ("D", "F", 6),
        ("E", "F", 8),
        ("E", "G", 9),
        ("F", "G", 11)
    ]
    g2 = Graph()
    g2.buildGraph(edges)
    g2.printGraph()
    print ("Find the shortest path with Dijkstra")
    print ("A -> E:")
    print((g2.shortestPath("A", "E")))

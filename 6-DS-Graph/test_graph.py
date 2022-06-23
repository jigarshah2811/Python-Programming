from Graph import Graph

"""
TEST CASES
"""
print("\n============ Directed Graph ==============\n")
g = Graph()
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
    ("F", "G", 11),
    ("H", "I", 20)
]
for edge in edges:
    src, dest = edge[0], edge[1]
    g.add_edge(src, dest)


print(("Graph: {0}".format(sorted(iter(g.graph.items()), key=lambda x:x[0]))))
print("DFS---> connected graph")
print((g.dfs_connected_graph("A")))

print("DFS---> Disconnected graph")
print((g.dfs_disconnected_graph()))

print("BFS---> connected graph")
print((g.bfs_connected_graph('A')))

print("BFS---> Disconnected graph")
print((g.bfs_disconnected_graph()))


print("\n============ Weighted directed Graph ==============\n")
g = Graph()
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
    ("G", "A", 9),
    ("F", "G", 11),
    ("H", "I", 20)
]
for edge in edges:
    src, dest, weight = edge[0], edge[1], edge[2]
    g.add_edge(src, dest, weight)


print(("Graph: {0}".format(sorted(iter(g.graph.items()), key=lambda x:x[0]))))
print("DFS---> Weighted Disconnected graph")
print((g.dfs_disconnected_graph()))

print("BFS---> Weighted Disconnected graph")
print((g.bfs_disconnected_graph()))

print("Detect Cycle---> Weighted Disconnected graph")
print((g.is_cycle()))

print("Find Path from Src to Dest---> Weighted Disconnected graph")
print((g.find_path("A", "G")))

clonedGraph = g.cloneGraph("A")
print("Original Graph: -->")
print(g.printGraph())
print("Cloned Graph: -->")
print(clonedGraph.printGraph())
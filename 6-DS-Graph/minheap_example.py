"""
Used for many Graph problems
PATTERN: Shortest path Djikstra (Pick up node with min cost to visit)
Minimum Spanning Tree
Topological sorting (Pick up node with least indegree to visit = resolve lowest in stack dependancy

"""


import heapq
edges = [
    ("B", "C", 8),
    ("B", "D", 9),
    ("B", "E", 7),
    ("C", "E", 5),
    ("D", "E", 15),
    ("D", "F", 6),
    ("E", "F", 8),
    ("E", "G", 9),
    ("F", "G", 11),
    ("A", "B", 7),
    ("A", "D", 5)
]

q = []
for edge in edges:
    heapq.heappush(q, edge)

for edge in edges:
    print((heapq.heappop(q)))

# Sort by 3rd param of list elements
print(heapq.nsmallest(10, edges, key=lambda x: x[2]))   # lambda function says, key = 3rd param to sort (by Weight)

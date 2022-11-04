""" SHORTEST PATH: Weighted DAG with Dijkstra in Python using heapq

Watch video: https://www.youtube.com/watch?v=lAXZGERcDf4
solution: https://gist.github.com/hanfang/89d38425699484cd3da80ca086d78129
"""
import collections
import heapq

class GraphSolution:
    def __init__(self, edges) -> None:
        # Graph {
        #       "SRC" : [(DEST1, WEIGHT1), (DEST2, WEIGHT2), ... ]
        #}
        self.graph = collections.defaultdict(list)
    
        # edges = [("A", "B", 7),....]
        for src, dest, weight in edges:
            self.graph[src].append((dest, weight))

        print(f"Graph: {list(self.graph.keys())}")

    def shortestPath(self, source, sink):
        # Heap element: (weight, node, pathToReachHere)
        cost, source, path = 0, source, [source]
        q = [(cost, source, path)]
        visited = set()

        while q:
            heapq.heapify(q)
            (cost, node, path) = heapq.heappop(q)
            if node in visited: # Already visited == skip to visit again
                continue
            
            # Mark visited to prevent visiting again
            visited.add(node)

            # Is this sync node?
            if node == sink:        # Bingo we found the DESTINATION, return total cost to reach here
                return cost, path

            for (conn, c) in self.graph[node]:
                if conn in visited: # Already visited == skip to visit again
                    continue
                
                heapq.heappush(q, (cost + c, conn, path + [conn]))

        
        # sink NOT FOUND
        return float('inf'), []



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

    s = GraphSolution(edges=edges)
    
    print ("Find the shortest path with Dijkstra")
    print ("A -> E:")
    print(s.shortestPath("A", "E"))
    print ("A -> G:")
    print(s.shortestPath("A", "G"))
    print ("B -> G:")
    print(s.shortestPath("B", "G"))
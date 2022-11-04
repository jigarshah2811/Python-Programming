"""
Greedy Algorithms | Set 2 (Kruskal’s Minimum Spanning Tree Algorithm)
http://www.geeksforgeeks.org/greedy-algorithms-set-2-kruskals-minimum-spanning-tree-mst/

1. Sort all the edges in non-decreasing order of their weight.

2. Pick the smallest edge. Check if it forms a cycle with the spanning tree
formed so far. If cycle is not formed, include this edge. Else, discard it.

3. Repeat step#2 until there are (V-1) edges in the spanning tree.

"""


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def __add_edge__(self, u, v, w):
        self.graph.append([u, v, w])

    def find_parent(self, parent, x):
        if parent[x] == x:
            return x
        return self.find_parent(parent, parent[x])

    def union(self, parent, rank, x, y):
        xRoot = self.find_parent(parent, x)
        yRoot = self.find_parent(parent, y)

        # (Union by Rank)
        # Attach the smaller rank tree under root of higher rank tree
        if rank[xRoot] > rank[yRoot]:
            parent[yRoot] = xRoot
        elif rank[xRoot] < rank[yRoot]:
            parent[xRoot] = yRoot
        else:
            # If ranks are same, pick one as root and increase rank
            parent[yRoot] = xRoot
            rank[xRoot] += 1

    def KruskalMST(self):
        result = []

        gi = 0
        ri = 0

        # Step 1) Sort all edges by weight
        self.graph = sorted(self.graph, key=lambda item:item[2])

        # Create empty subsets for parent & rank to follow Union-Find algo
        parent = []; rank = []
        for node in xrange(self.V):
            parent.append(node)
            rank.append(-1)

        # Base case
        while ri < self.V - 1:
            # Step 2) Pick up sorted weight edge
            # print gi

            u, v, w = self.graph[gi]
            gi += 1

            # Step 3) Check if cycle is formed
            x_subset = self.find_parent(parent, u)
            y_subset = self.find_parent(parent, v)
            if x_subset != y_subset:
                # No Cycle ---> Add this in result. Add in union for next cycle
                # & Repeat 2)
                ri += 1
                result.append([u, v, w])
                self.union(parent, rank, x_subset, y_subset)
            # Cycle ---> Discard the edge
            # & Repeat 2)

        return result


def main():
    g = Graph(4)
    g.__add_edge__(0, 1, 10)
    g.__add_edge__(0, 2, 6)
    g.__add_edge__(0, 3, 5)
    g.__add_edge__(1, 3, 15)
    g.__add_edge__(2, 3, 4)
    print g.KruskalMST()


if __name__ == "__main__":
    main()









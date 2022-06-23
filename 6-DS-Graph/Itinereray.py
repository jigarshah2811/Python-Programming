"""
https://leetcode.com/problems/reconstruct-itinerary/

PATTERN: Finding a cycle in graph.... DFS with recordingStack
"""

import collections

class Graph(object):
    def __init__(self):
        self.graph = collections.defaultdict(list)

    # Weighted directed graph
    def add_edge(self, src, dest):
        self.graph[src].append(dest)

    def findItinerary(self, node):
        visited = list()
        recStack = collections.OrderedDict()
        visited.append(node)
        return self.dfsRecur(node, visited, recStack)

    def dfsRecur(self, node, visited, recStack):

        # Visit all connections (Skip the one's already in recording stack)
        for conn in sorted(self.graph[node]):   # Sorted: Because we are going in alpha lexical order!
            print(("Visiting from Node: {0}, Conn: {1}".format(node, conn)))
            if (node, conn) not in recStack:
                recStack[(node, conn)] = True
                visited.append(conn)
                recStack, visited = self.dfsRecur(conn, visited, recStack)

        return recStack, visited

    def printGraph(self):
        return sorted(list(self.graph.items()), key=lambda x: x[0])



g = Graph()
Input =  [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
for edge in Input:
    g.add_edge(edge[0], edge[1])

#print(g.printGraph())
print((g.findItinerary("JFK")[1]))

g = Graph()
Input = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
for edge in Input:
    g.add_edge(edge[0], edge[1])

#print(g.printGraph())
print((g.findItinerary("JFK")[1]))


g = Graph()
Input = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
for edge in Input:
    g.add_edge(edge[0], edge[1])

#print(g.printGraph())
print((g.findItinerary("JFK")[1]))
#Expected ["JFK","NRT","JFK","KUL"]
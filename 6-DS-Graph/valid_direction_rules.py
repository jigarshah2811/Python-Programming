"""
This problem was asked by Uber.

A rule looks like this:

A NE B

This means this means point A is located northeast of point B.

A SW C

means that point A is southwest of C.

Given a list of rules, check if the sum of the rules validate. For example:

A N B
B NE C
C N A
does not validate, since A cannot be both north and south of C.

A NW B
A N B
is considered valid.
"""
"""
Solution: An approach is to create adjency list... Graph1 for N and S direction, Graph2 for E and W direction
Then check if there's Cycle in any graph. To determine valid or invalid.
"""
import collections

class Graph():
    def __init__(self):
        self.g = collections.defaultdict(list)

    def __add_edge__(self, src, dest):
        self.g[src].append(dest)


class Solution:
    def isDirectionValid(self, rules):
        def detectcycle(node, path):
            if node in path: return True

            visited.add(node)
            path.add(node)
            for conn in g1.g[node]:
                if conn not in visited:
                    detectcycle(conn, path)

            path.remove(node)
            return False

        g1, g2 = Graph(), Graph()       # g1 for N, S traffic.... #g2 for E, W traffic
        for rule in rules:
            parts = rule.split(" ")
            if 'N' in parts[1]:
                g1.__add_edge__(parts[0], parts[2])
            if 'S' in parts[1]:
                g1.__add_edge__(parts[2], parts[0])
            if 'E' in parts[1]:
                g2.__add_edge__(parts[0], parts[2])
            if 'W' in parts[1]:
                g2.__add_edge__(parts[2], parts[0])

        print(("Graph: ", g1.g, g2.g))
        # Graph for NS and Graph for EW ready. Now check for cycles
        isCycleInG1, isCycleInG2 = False, False

        visited = set()
        for node in list(g1.g.keys()):
            isCycleInG1 = detectcycle(node, path=set())

        visited = set()
        for node in list(g2.g.keys()):
            isCycleInG2 = detectcycle(node, path=set())

        return not isCycleInG1 and not isCycleInG2


#print(Solution().isDirectionValid(rules=['A N B', 'B NE C', 'C N A']))
print((Solution().isDirectionValid(rules = ['A NW B', 'B NE C', 'C SE A'])))
#print(Solution().isDirectionValid(rules = ['A NW B', 'B NE C', 'C SE A', 'D NE A']))


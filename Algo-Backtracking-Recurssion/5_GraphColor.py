class Solution:

    def graphColor(self, graph, V, numColors):
        def isSafe(curV, c):
            # Check if this color is not applied to any connection of V.
            for i in range(V):
                print(("Checking vertex: [0]".format(curV)))
                if graph[curV][i] and c == color[i]:    # There is edge between curV and i, and that neighbour has same color
                    return False
            return True

        def backtrack(curV):
            # 1) Base case: If all vertex are colored, then we found solution
            if curV == V:
                return True
            # 2) Breath ---> Possible moves are to select any from available colors
            for c in range(1, numColors+1):
                # 3) Check if it's safe to apply this color to vertex
                if isSafe(curV, c):
                    # 4) Apply this color
                    print(("vertex:[0] color:[1]".format(curV, c)))
                    color[curV] = c

                    # 5) Recursively apply available colors to next vertex
                    if backtrack(curV+1):
                        return True

                    # 6) Backtrack: If we can't find solution recursively for all vertexes
                    print(("Backtrack vertex:[0] color:[1]".format(curV, c)))
                    color[curV] = 0

            return False

        color = [0] * V
        backtrack(0)
        return color


s = Solution()
graph = [[0, 1, 1, 1], 
        [1, 0, 1, 0], 
        [1, 1, 0, 1], 
        [1, 0, 1, 0]]
print((s.graphColor(graph=graph, V=4, numColors=3)))

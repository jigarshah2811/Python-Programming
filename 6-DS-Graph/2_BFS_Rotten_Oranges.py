import collections
"""
https://leetcode.com/problems/rotting-oranges/submissions/

PATTERN: Classic example of BFS at each level! (At Each level of BFS, Crawl to conns once!)

"""
import collections
from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        rows, cols = len(grid), len(grid[0])

        good = 0  # Count # of good oranges, to verify all gets rotten at end
        totalTime = 0  # For each BFS Phase level
        q = collections.deque()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:  # good
                    good += 1
                if grid[row][col] == 2:  # rotten
                    q.append((row, col))

        print(("Starting rotten from q:", q))

        def DFS():
            nonlocal good                                   # Python3: How to use enclosed var scope in local fun
            nonlocal totalTime
            while q:
                nodes = len(q)
                while nodes > 0:  # Each stage, do 1 BFS for all rotten entries
                    (row, col) = q.popleft()  # Get rotten orange
                    print(("Processing rotten: ", (row, col)))
                    for (connRow, connCol) in [(row + 1, col), (row, col + 1), (row - 1, col), (row, col - 1)]:
                        # If this is good orange
                        if 0 <= connRow < rows and 0 <= connCol < cols and grid[connRow][connCol] == 1:
                            print(("Rotting: ", (connRow, connCol)))
                            grid[connRow][connCol] = 2  # Rotten this conn
                            q.append((connRow, connCol))
                            good -= 1
                    nodes -= 1

                # At this level, made all conn rotten
                totalTime += 1
        DFS()
        return max(0, totalTime - 1) if good == 0 else -1


s = Solution()
grid = [[2,1,1],[1,1,0],[0,1,1]]
print((s.orangesRotting(grid)))




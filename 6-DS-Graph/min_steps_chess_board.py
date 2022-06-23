"""
Matrix: Chess board: Min step to reach from Src to Dest location for a knight
https://www.geeksforgeeks.org/minimum-steps-reach-target-knight/

Pattern: BFS
"""
ROWS = 8
COLS = 8
class Solution(object)adfa
    def minPath(self, src_x, src_y, dest_x, dest_y):
        def isSafe(x, y):
            if 0 <= x < ROWS and 0 <= y < COLS:
                return True
            return False

        # Breath --> All possible neighbors of this cell
        step_x = [2, 2, -2, -2, 1, 1, -1, -1]
        step_y = [1, -1, 1, -1, 2, -2, 2, -2]

        visited = set()
        q = [(src_x, src_y)]        # Start with SRC point
        curBFSLevel = 0
        while q:

            # In order to maintain the LEVEL for BFS
            n = len(q)
            while n > 0:
                n -= 1
                (cur_x, cur_y) = q.pop()
                visited.add((cur_x, cur_y))

                if (cur_x, cur_y) == (dest_x, dest_y)    # Found destination
                    return curBFSLevel

                for i in range(8):
                    next_x = cur_x + step_x[i]
                    next_y = cur_y + step_y[i]

                    if isSafe(next_x, next_y) and (next_x, next_y) not in visited:
                        q.append((next_x, next_y))

            curBFSLevel += 1

        return -1       # Not Found


s = Solution()
#print(s.minPath(0,0,7,7,8))
#print(s.minPath(1,1,30,30,30))
#print((s.minPath(1,3,5,0,8)))

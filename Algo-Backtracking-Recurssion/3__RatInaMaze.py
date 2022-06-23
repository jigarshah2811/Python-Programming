"""
https://www.geeksforgeeks.org/rat-in-a-maze-backtracking-2/
"""
class Solution():
    def rateInaMaze(self, board):
        def isSafe(x, y):
            # Check cell (x, y) is not OOB and rat can go there's no wall
            if (0 <= x < M) and (0 <= y < N) and board[x][y]:
                return True
            return False

        def backtrack(x, y):
            # 1) Base case. Found solution if rat reached destination?
            if (x == M - 1) and (y == N - 1):
                sol[x][y] = 1
                return True

            # 2) Breath ---> For all possible comb that Rat can move. Horizontal or Diag
            # 3) See if cell (x,y) is safe for rat to move
            if isSafe(x, y):
                # 4) Move here
                sol[x][y] = 1

                # 5) Recur check if this move can lead to solution Horizontal or Diag
                if backtrack(x + 1, y):
                    return True
                if backtrack(x, y + 1):
                    return True

                # 6) Backtrack, if sol is not reachable from this move
                sol[x][y] = -1

            return False

        M = len(board)
        N = len(board[0])
        sol = [[-1 for i in range(M)] for i in range(N)]
        backtrack(0, 0)
        return sol


s = Solution()
# Initialize the maze, there is clear path for rat to reach from (0,0) to (M-1, N-1)
board = [[1, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 1, 0, 0],
        [1, 1, 1, 1]]
print((s.rateInaMaze(board)))

# Initialize the maze, there is NO path for rat to reach from (0,0) to (M-1, N-1)
board = [[1, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 1, 0, 0],
        [1, 1, 0, 1]]
print((s.rateInaMaze(board)))
